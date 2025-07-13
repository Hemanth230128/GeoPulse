import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Load national risk score data
national_df = pd.read_csv('India_risk_factor.csv')  # Columns: Year, Risk_Factor

# Prepare features and target
X = national_df[['Year']].values
y = national_df['Risk_Factor'].values

# Scale the year feature for ML models
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Define advanced ML models
models = {
    'RandomForest': RandomForestRegressor(random_state=42),
    'GradientBoosting': GradientBoostingRegressor(random_state=42),
    'MLP': MLPRegressor(random_state=42, max_iter=1000)
}

# Hyperparameter grids for tuning
param_grids = {
    'RandomForest': {
        'n_estimators': [50, 100],
        'max_depth': [3, 5, None]
    },
    'GradientBoosting': {
        'n_estimators': [50, 100],
        'learning_rate': [0.01, 0.1],
        'max_depth': [3, 5]
    },
    'MLP': {
        'hidden_layer_sizes': [(50,), (100,)],
        'activation': ['relu'],
        'solver': ['adam'],
        'alpha': [0.0001, 0.001]
    }
}

# Time series split for cross-validation
tscv = TimeSeriesSplit(n_splits=5)
best_models = {}

# Model selection and tuning
for name, model in models.items():
    grid = GridSearchCV(model, param_grids[name], cv=tscv, scoring='neg_mean_squared_error')
    grid.fit(X_scaled, y)
    best_models[name] = grid.best_estimator_
    print(f"Best params for {name}: {grid.best_params_}")

# Select the model with the lowest MSE
best_model_name = None
best_score = float('inf')
for name, model in best_models.items():
    preds = model.predict(X_scaled)
    mse = mean_squared_error(y, preds)
    print(f"MSE for {name}: {mse}")
    if mse < best_score:
        best_score = mse
        best_model_name = name

print(f"Selected best model: {best_model_name}")

# Predict national risk scores for 2025–2030
future_years = np.arange(2025, 2031).reshape(-1, 1)
future_years_scaled = scaler.transform(future_years)
national_pred = best_models[best_model_name].predict(future_years_scaled)

# Load district-level risk data
district_df = pd.read_csv('district_risk_scores.csv')  # Columns: State, District, RiskScore_2015, RiskScore_2019

# Calculate proportions for 2015 and 2019
nat_2015 = national_df[national_df['Year'] == 2015]['Risk_Factor'].values[0]
nat_2019 = national_df[national_df['Year'] == 2019]['Risk_Factor'].values[0]

district_df['Prop_2015'] = district_df['RiskScore_2015'] / nat_2015
district_df['Prop_2019'] = district_df['RiskScore_2019'] / nat_2019
district_df['Avg_Prop'] = district_df[['Prop_2015', 'Prop_2019']].mean(axis=1)

# Predict district risk scores for 2025–2030
predictions = []
for idx, year in enumerate(range(2025, 2031)):
    nat_score = national_pred[idx]
    for _, row in district_df.iterrows():
        pred_score = nat_score * row['Avg_Prop']
        predictions.append({
            'State': row['State'],
            'District': row['District'],
            'Year': year,
            'Predicted_RiskScore': pred_score
        })

pred_df = pd.DataFrame(predictions)
pred_df.to_csv('district_risk_score_predictions_2025_2030_advanced.csv', index=False)
print(pred_df.head())
