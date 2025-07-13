import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# === 1. Load Data ===
national = pd.read_csv('data_risk_with_factor.csv')
district = pd.read_csv('district_risk_scores_2015_2019.csv')

# === 2. Helper: Forecast a Field Using Linear Regression ===
def forecast_field(field):
    X = national[['Year']].values
    y = national[field].values
    model = LinearRegression()
    model.fit(X, y)
    future_years = np.arange(2025, 2031).reshape(-1, 1)
    preds = model.predict(future_years)
    return preds

# === 3. Forecast All National Fields ===
fields = ['Sanitation', 'Literacy', 'Child_Population_Growth', 'Risk_Factor']
future_preds = {field: forecast_field(field) for field in fields}
future_years = np.arange(2025, 2031)

# === 4. Calculate District Proportions for 2015 and 2019 ===
nat_2015 = national[national['Year'] == 2015].iloc[0]
nat_2019 = national[national['Year'] == 2019].iloc[0]

district['Sanitation_prop_2015'] = district['Sanitation_2015'] / nat_2015['Sanitation']
district['Sanitation_prop_2019'] = district['Sanitation_2019'] / nat_2019['Sanitation']
district['Sanitation_prop_avg'] = district[['Sanitation_prop_2015', 'Sanitation_prop_2019']].mean(axis=1)

district['Literacy_prop_2015'] = district['Literacy_2015'] / nat_2015['Literacy']
district['Literacy_prop_2019'] = district['Literacy_2019'] / nat_2019['Literacy']
district['Literacy_prop_avg'] = district[['Literacy_prop_2015', 'Literacy_prop_2019']].mean(axis=1)

district['ChildPop_prop_2015'] = district['ChildPop_2015'] / nat_2015['Child_Population_Growth']
district['ChildPop_prop_2019'] = district['ChildPop_2019'] / nat_2019['Child_Population_Growth']
district['ChildPop_prop_avg'] = district[['ChildPop_prop_2015', 'ChildPop_prop_2019']].mean(axis=1)

district['RiskScore_prop_2015'] = district['RiskScore_2015'] / nat_2015['Risk_Factor']
district['RiskScore_prop_2019'] = district['RiskScore_2019'] / nat_2019['Risk_Factor']
district['RiskScore_prop_avg'] = district[['RiskScore_prop_2015', 'RiskScore_prop_2019']].mean(axis=1)

# === 5. Predict District-Level Values for 2025–2030 ===
records = []
for idx, year in enumerate(future_years):
    for _, row in district.iterrows():
        records.append({
            'State': row['State'],
            'District': row['District'],
            'Year': year,
            'Sanitation': future_preds['Sanitation'][idx] * row['Sanitation_prop_avg'],
            'Literacy': future_preds['Literacy'][idx] * row['Literacy_prop_avg'],
            'Child_Population_Growth': future_preds['Child_Population_Growth'][idx] * row['ChildPop_prop_avg'],
            'Risk_Factor': future_preds['Risk_Factor'][idx] * row['RiskScore_prop_avg'],
        })

df_out = pd.DataFrame(records)

# === 6. Replace values >= 1 with state mean (computed from values < 1) ===
def replace_ge1_with_state_mean(df, col):
    for year in df['Year'].unique():
        year_mask = df['Year'] == year
        for state in df.loc[year_mask, 'State'].unique():
            state_mask = (df['State'] == state) & year_mask
            valid_mask = state_mask & (df[col] < 1)
            if valid_mask.any():
                state_mean = df.loc[valid_mask, col].mean()
                df.loc[state_mask & (df[col] >= 1), col] = state_mean
            else:
                df.loc[state_mask & (df[col] >= 1), col] = 1
    return df

for col in ['Sanitation', 'Literacy', 'Child_Population_Growth']:
    df_out = replace_ge1_with_state_mean(df_out, col)

df_out.to_csv('district_forecast_2025_2030_all_fields_linear.csv', index=False)
print(df_out.head())
