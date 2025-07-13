import pandas as pd

# Load the CSV files
numbirth_df = pd.read_csv('numbirth.csv')
population_df = pd.read_csv('population_IND.csv')
death_rate_df = pd.read_csv('death_rate.csv')

# Filter for India, Total, and correct indicator for each file
numbirth_filtered = numbirth_df[
    (numbirth_df['REF_AREA:Geographic area'] == 'IND: India') &
    (numbirth_df['SEX:Sex'] == '_T: Total') &
    (numbirth_df['INDICATOR:Indicator'] == 'DM_BRTS: Number of births')
][['TIME_PERIOD:Time period', 'OBS_VALUE:Observation Value']].rename(
    columns={'TIME_PERIOD:Time period': 'Year', 'OBS_VALUE:Observation Value': 'Number_of_Births'}
)

population_filtered = population_df[
    (population_df['REF_AREA:Geographic area'] == 'IND: India') &
    (population_df['SEX:Sex'] == '_T: Total') &
    (population_df['INDICATOR:Indicator'] == 'DM_POP_TOT: Total population')
][['TIME_PERIOD:Time period', 'OBS_VALUE:Observation Value']].rename(
    columns={'TIME_PERIOD:Time period': 'Year', 'OBS_VALUE:Observation Value': 'Total_Population'}
)

death_rate_filtered = death_rate_df[
    (death_rate_df['REF_AREA:Geographic area'] == 'IND: India') &
    (death_rate_df['SEX:Sex'] == '_T: Total') &
    (death_rate_df['INDICATOR:Indicator'] == 'CME_MRY1T4: Child mortality rate (aged 1-4 years)')
][['TIME_PERIOD:Time period', 'OBS_VALUE:Observation Value']].rename(
    columns={'TIME_PERIOD:Time period': 'Year', 'OBS_VALUE:Observation Value': 'Child_Mortality_Rate'}
)

# Merge all dataframes on Year
merged_df = pd.merge(numbirth_filtered, population_filtered, on='Year')
merged_df = pd.merge(merged_df, death_rate_filtered, on='Year')

# Convert columns to numeric
merged_df['Number_of_Births'] = pd.to_numeric(merged_df['Number_of_Births'])
merged_df['Total_Population'] = pd.to_numeric(merged_df['Total_Population'])
merged_df['Child_Mortality_Rate'] = pd.to_numeric(merged_df['Child_Mortality_Rate'])

# Calculate Birth Rate: (Number of Births / Total Population) * 1000
merged_df['Birth_Rate'] = (merged_df['Number_of_Births'] / merged_df['Total_Population']) * 1000

# Calculate Child Population Growth: Birth Rate - Death Rate
merged_df['Child_Population_Growth'] = merged_df['Birth_Rate'] - merged_df['Child_Mortality_Rate']

# Output only Year and Child Population Growth
result_df = merged_df[['Year', 'Child_Population_Growth']]

# Save to CSV
result_df.to_csv('child_population_growth.csv', index=False)
