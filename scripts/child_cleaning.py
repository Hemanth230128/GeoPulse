import pandas as pd

# Load datasets
child_df = pd.read_csv('../data/raw/childpop.csv')
land_df = pd.read_csv('../data/raw/land_area.csv')

# Filter child population data for years 2000-2023
child_df = child_df[(child_df['Year'] >= 2000) & (child_df['Year'] <= 2023)]

# Rename the long population column for convenience
pop_col = 'Population - Sex: all - Age: 0-4 - Variant: estimates'
child_df.rename(columns={pop_col: 'Population'}, inplace=True)

# Convert columns to numeric, coercing errors to NaN
child_df['Population'] = pd.to_numeric(child_df['Population'], errors='coerce')
land_df['Land area (sq. km)'] = pd.to_numeric(land_df['Land area (sq. km)'], errors='coerce')

# Remove zero or missing land area values to avoid division errors
land_df = land_df[land_df['Land area (sq. km)'] > 0]

# Use unique land area values per Entity and Code
land_unique = land_df[['Entity', 'Code', 'Land area (sq. km)']].drop_duplicates()

# Merge child population data with land area data on Entity and Code
merged_df = pd.merge(child_df, land_unique, on=['Entity', 'Code'], how='left')

# Calculate population density
merged_df['Population Density'] = merged_df['Population'] / merged_df['Land area (sq. km)']

# Select only required columns for final output
final_df = merged_df[['Entity', 'Code', 'Year', 'Population Density']]

# Save the final cleaned dataset with population density
final_df.to_csv('../data/cleaned/children_population_density.csv', index=False)

print("✅ Population density calculated and saved successfully!")
