"""
Forecast WPR, Literacy, Child-Population-Growth and Risk-Factor for every
district (2025-2030) and save them to `district_forecast_2025_2030_all_fields.csv`.

Assumptions
-----------
• National time–series  : data_risk_with_factor.csv  
    required columns    : Year, WPR, Literacy, Child_Population_Growth,
                          Risk_Factor  (or RiskScore)  
• District 2011 snapshot: combined_2001_2011.csv  
    required columns    : Name, WPR, Literacy Rate, ChildPopGrowth,
                          RiskScore (Risk_Factor optional), State (optional)
"""

import warnings, numpy as np, pandas as pd
from sklearn.ensemble       import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model   import LinearRegression
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn.preprocessing   import StandardScaler
from sklearn.metrics         import mean_squared_error
from sklearn.exceptions      import ConvergenceWarning

warnings.filterwarnings("ignore", category=ConvergenceWarning)

# ───────────────────────────── 1 ▸ LOAD & CLEAN ──────────────────────────────
nat  = pd.read_csv("../data/merged/ind_risk_score.csv")
dist = pd.read_csv("../data/merged/combined_2001_2011.csv")

# harmonise column names ------------------------------------------------------
nat = nat.rename(columns={
    "Child_Population_Growth": "ChildPopGrowth",
    "Risk_Factor"            : "RiskScore"
})
dist = dist.rename(columns={
    "Literacy Rate"          : "Literacy",
    "Risk_Factor"            : "RiskScore"
})

need_nat  = {"Year", "WPR", "Literacy", "ChildPopGrowth", "RiskScore"}
need_dist = {"Name", "WPR", "Literacy", "ChildPopGrowth", "RiskScore"}
if not need_nat.issubset(nat.columns):
    missing = need_nat - set(nat.columns)
    raise ValueError(f"National file missing columns: {missing}")
if not need_dist.issubset(dist.columns):
    missing = need_dist - set(dist.columns)
    raise ValueError(f"District file missing columns: {missing}")

# ───────────────────────────── 2 ▸ FORECASTER ────────────────────────────────
def forecast_series(field: str, years: list[int]) -> pd.Series:
    X = nat[["Year"]].values
    y = nat[field].values
    scaler   = StandardScaler().fit(X)
    X_scaled = scaler.transform(X)
    cv       = TimeSeriesSplit(n_splits=3)

    # candidate models
    models = {
        "RF":  (RandomForestRegressor(random_state=42),
                {"n_estimators":[200], "max_depth":[None,5]}),
        "GB":  (GradientBoostingRegressor(random_state=42),
                {"n_estimators":[300], "learning_rate":[0.03], "max_depth":[3]}),
        "MLP": (MLPRegressor(random_state=42, max_iter=3000, early_stopping=True),
                {"hidden_layer_sizes":[(64,32)], "alpha":[1e-3]}),
        "LR":  (LinearRegression(), {})          # fallback – always fits
    }

    best_est, best_mse = None, np.inf
    for est, grid in models.values():
        if grid:            # Grid-search models
            gs = GridSearchCV(est, grid, cv=cv,
                              scoring="neg_mean_squared_error",
                              n_jobs=-1, error_score="raise")
            try:
                gs.fit(X_scaled, y)
                mse = -gs.best_score_
                if mse < best_mse:
                    best_est, best_mse = gs.best_estimator_, mse
            except Exception:
                continue
        else:               # Linear regression fallback
            est.fit(X_scaled, y)
            mse = mean_squared_error(y, est.predict(X_scaled))
            if mse < best_mse:
                best_est, best_mse = est, mse

    future_scaled = scaler.transform(np.array(years).reshape(-1,1))
    return pd.Series(best_est.predict(future_scaled), index=years)

years   = list(range(2025, 2031))
nat_fc  = {col: forecast_series(col, years) for col in
           ["WPR", "Literacy", "ChildPopGrowth", "RiskScore"]}

# ───────────────────────────── 3 ▸ 2011 OFFSETS ──────────────────────────────
nat11 = nat.loc[nat["Year"] == 2011].iloc[0]

# additive deltas
dist["Δ_WPR"]   = dist["WPR"]            - nat11["WPR"]
dist["Δ_Lit"]   = dist["Literacy"]       - nat11["Literacy"]
dist["Δ_Child"] = dist["ChildPopGrowth"] - nat11["ChildPopGrowth"]

# multiplicative ratio for RiskScore
dist["Risk_ratio"] = dist["RiskScore"] / nat11["RiskScore"]

# ───────────────────────────── 4 ▸ BUILD GRID ────────────────────────────────
rows = []
for y in years:
    nW = nat_fc["WPR"][y]
    nL = nat_fc["Literacy"][y]
    nC = nat_fc["ChildPopGrowth"][y]      # can be ±
    nR = nat_fc["RiskScore"][y]

    for _, r in dist.iterrows():
        rows.append({
            "District"                : r["Name"],
            "State"                   : r.get("State", np.nan),
            "Year"                    : y,
            "WPR"                     : np.clip(nW + r["Δ_WPR"], 0, 100),
            "Literacy"                : np.clip(nL + r["Δ_Lit"], 0, 100),
            "Child_Population_Growth" : nC + r["Δ_Child"],
            "Risk_Factor"             : np.clip(nR * r["Risk_ratio"], 0, 1)
        })

df = pd.DataFrame(rows)

# ───────────── 5 ▸ OPTIONAL: SMOOTH OUT WPR & LITERACY OUTLIERS ─────────────
for col in ["WPR", "Literacy"]:
    for y in years:
        slice_y = df[df["Year"] == y]
        for st in slice_y["State"].dropna().unique():
            mask   = (df["Year"] == y) & (df["State"] == st)
            normal = df.loc[mask & (df[col] < 100), col]
            if not normal.empty:
                df.loc[mask & (df[col] >= 100), col] = normal.mean()

# ───────────────────────────── 6 ▸ SAVE OUTPUT ──────────────────────────────
(df
 .drop(columns="State")
 .to_csv("district_forecast_2025_2030_all_fields.csv",
         index=False,
         float_format="%.6f"))

print("✓ district_forecast_2025_2030_all_fields.csv written")
