import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Load Data
national_df = pd.read_csv('India_risk_factor.csv')  # Columns: Year, Risk_Factor
district_df = pd.read_csv('district_risk_scores.csv')  # Columns: State, District, RiskScore_2015, RiskScore_2019

# 2. Train Regression Model on National Data
X = national_df[['Year']].values
y = national_df['Risk_Factor'].values
model = LinearRegression()
model.fit(X, y)

# Predict national risk scores for 2025–2030
future_years = np.arange(2025, 2031).reshape(-1, 1)
national_pred = model.predict(future_years)

# 3. Calculate District Proportions for 2015 and 2019
nat_2015 = national_df[national_df['Year'] == 2015]['Risk_Factor'].values[0]
nat_2019 = national_df[national_df['Year'] == 2019]['Risk_Factor'].values[0]

district_df['Prop_2015'] = district_df['RiskScore_2015'] / nat_2015
district_df['Prop_2019'] = district_df['RiskScore_2019'] / nat_2019
district_df['Avg_Prop'] = district_df[['Prop_2015', 'Prop_2019']].mean(axis=1)

# 4. Predict District Risk Scores for 2025–2030
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

# 5. Save Results
pred_df.to_csv('district_risk_score_predictions_2025_2030.csv', index=False)
print(pred_df.head())
