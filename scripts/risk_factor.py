import pandas as pd

# Load the data
df = pd.read_csv('data_risk.csv')

# Normalize the columns
df['WPR_norm'] = df['WPR'] / 100
df['Literacy_norm'] = df['Literacy']
df['ChildPopGrowth_norm'] = df['Child_Population_Growth'] / 10

# Define weights (adjust as needed)
w1 = 0.12
w2 = 0.48
w3 = 0.4

# Calculate the risk factor
df['Risk_Factor'] = (
    w1 * (1 - df['WPR_norm']) +
    w2 * (1 - df['Literacy_norm']) +
    w3 * df['ChildPopGrowth_norm']
)

# Optionally, drop the normalized columns
df_final = df[['Year', 'WPR', 'Literacy', 'Child_Population_Growth', 'Risk_Factor']]

# Save to a new CSV
df_final.to_csv('data_risk_with_factor.csv', index=False)
