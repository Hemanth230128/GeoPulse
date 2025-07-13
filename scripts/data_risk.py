import pandas as pd

# Load the CSV files
child_population_growth = pd.read_csv('child_population_growth.csv')
literacy = pd.read_csv('literacy_forecast.csv')
WPR = pd.read_csv('WPR.csv')

# Filter WPR data for India and the correct indicator
WPR_ind = WPR[
    (WPR['Country'] == 'IND: India') &
    (WPR['Indicator'] == 'WS_PPL_S-ALB: Proportion of population using at least basic WPR services')
]


# Prepare WPR dataframe for merging
WPR_final = WPR_ind[['Year', 'Value']].rename(columns={'Value': 'WPR'})

# Merge all dataframes on 'Year'
merged_df = pd.merge(child_population_growth, literacy, on='Year')
merged_df = pd.merge(merged_df, WPR_final, on='Year')

# Reorder columns as requested
merged_df = merged_df[['Year', 'WPR', 'Literacy', 'Child_Population_Growth']]

# Save to CSV
merged_df.to_csv('data_risk.csv', index=False)
