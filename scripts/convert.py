import pandas as pd

# Replace 'path/to/merged.csv' with your actual merged CSV file path
df = pd.read_csv('../data/merged/final_merged_data.csv')

# Save as JSON - list of records (objects)
df.to_json('../data/merged/final_merged_data.json', orient='records')
