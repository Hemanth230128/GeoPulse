import pandas as pd
import numpy as np

# Load datasets
elec = pd.read_csv('cleaned_accesstoelec.csv')
pop = pd.read_csv('cleaned_population_density.csv')
gdp = pd.read_csv('GDP_Growth_Filled.csv')

# Standardize and rename columns
elec = elec.rename(columns={
    'Entity': 'Country',
    'Code': 'Country Code',
    'Access to electricity (% of population)': 'accesstoelec'
})
pop = pop.rename(columns={
    'Country': 'Country',
    'Country Code': 'Country Code',
    'Population_Density': 'Population_Density'
})
# GDP data is in wide format, so melt to long
gdp_long = gdp.melt(
    id_vars=['Country Name', 'Country Code', 'Indicator Name'],
    var_name='Year',
    value_name='GDP_Growth'
)
gdp_long = gdp_long[gdp_long['Indicator Name'] == 'GDP growth (annual %)']
gdp_long = gdp_long.rename(columns={'Country Name': 'Country'})
gdp_long['Year'] = gdp_long['Year'].astype(float).astype(int)

# Ensure year columns are int for merging
elec['Year'] = elec['Year'].astype(int)
pop['Year'] = pop['Year'].astype(float).astype(int)

# Merge datasets on Country Code and Year
df = pd.merge(pop, elec[['Country Code', 'Year', 'accesstoelec']], on=['Country Code', 'Year'], how='inner')
df = pd.merge(df, gdp_long[['Country', 'Country Code', 'Year', 'GDP_Growth']], on=['Country', 'Country Code', 'Year'], how='left')

# --- Deprivation Functions ---

def deprive_elec(x):
    if pd.isnull(x): return np.nan
    return 1 - min(max(x, 0), 100) / 100

def deprive_density(x):
    if pd.isnull(x):
        return np.nan
    if x <= 50:
        return 0
    elif x >= 300:
        return 1
    else:
        return (x - 50) / (300 - 50)


def deprive_gdp(x):
    if pd.isnull(x): return np.nan
    if x <= -2: return 1
    elif x < 1: return (1 - x) / 3
    else: return 0

# Apply continuous scaling
df['deprived_elec'] = df['accesstoelec'].apply(deprive_elec)
df['deprived_density'] = df['Population_Density'].apply(deprive_density)
df['deprived_gdp'] = df['GDP_Growth'].apply(deprive_gdp)

# Weighted MPI (equal weights)
df['MPI'] = (
    df['deprived_elec'] * (1/3) +
    df['deprived_density'] * (1/3) +
    df['deprived_gdp'] * (1/3)
)

# Select relevant columns and save
out_cols = ['Country', 'Country Code', 'Year', 'Population_Density', 'accesstoelec', 'GDP_Growth', 'MPI']
df[out_cols].to_csv('povertyindex.csv', index=False)
