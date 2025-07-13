import pandas as pd


# Load the dataset
df = pd.read_csv('../data/raw/malnutrition.csv')

# Drop rows where all the year columns (2000 onwards) are NaN
# Adjust '2000' if your year columns start at a different year
df_cleaned = df.dropna(subset=df.columns[5:], how='all')

# Save the cleaned dataset
df_cleaned.to_csv('../data/cleaned/malnutrition_cleaned.csv', index=False)

print("✅ Empty rows removed and saved as: ../data/cleaned/malnutrition_cleaned.csv")