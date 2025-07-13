import pandas as pd

child_df = pd.read_csv('../data/cleaned/child_pop_growth_india.csv') 
literacy_df = pd.read_csv('../data/cleaned/literacy_india.csv')  
wpr_df = pd.read_csv('../data/cleaned/wpr_india.csv')  

# Merge dataframes on common key (e.g., 'Year')
merged_df = child_df.merge(literacy_df, on='Year').merge(wpr_df, on='Year')

# Apply the formula
merged_df['RiskScore'] = (
    0.4 * merged_df['ChildPopGrowth'] +
    0.48 * (1 - merged_df['Literacy'] / 100) +
    0.12 * (1 - merged_df['WPR'] / 100)
)

final_df = merged_df[['Year', 'ChildPopGrowth', 'WPR', 'RiskScore']]

# Save to new CSV
final_df.to_csv('../data/merged/ind_risk_score.csv', index=False)

print("File 'ind_risk_score.csv' created with columns: Year, ChildPopGrowth, WPR, RiskScore")