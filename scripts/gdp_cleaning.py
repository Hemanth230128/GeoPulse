import pandas as pd

# Load your dataset
df = pd.read_csv('../data/raw/GDP_Growth.csv')

# Fill missing values using interpolation
df_interpolated = df.interpolate(method='linear', axis=0).fillna(method='bfill').fillna(method='ffill')

# Save the filled data to a new CSV file
df_interpolated.to_csv('../data/cleaned/GDP_Growth_Filled.csv', index=False)

print("✅ Missing values filled and saved as 'GDP_Growth_Filled.csv'")