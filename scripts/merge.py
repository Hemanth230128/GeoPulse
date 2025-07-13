import pandas as pd
import numpy as np

# --- 1. Load both datasets ---
mpi_df = pd.read_csv("mpi_interpolated.csv")  # Columns: Country, Year, Value
pop_df = pd.read_csv("population_density.csv")  # Columns: Country, Country Code, Year, Population_Density

# --- 2. Interpolate MPI within each country ---
def interpolate_mpi(group):
    group = group.sort_values('Year').reset_index(drop=True)
    years = group['Year'].values
    values = group['Value'].values

    full_years = np.arange(years.min(), years.max() + 1)
    interpolated = pd.DataFrame({
        'Country': group['Country'].iloc[0],
        'Year': full_years
    })

    value_map = dict(zip(years, values))
    interpolated['Value'] = interpolated['Year'].map(value_map)
    interpolated['Value'] = interpolated['Value'].interpolate(method='linear', limit_area='inside')
    
    return interpolated

mpi_interpolated = mpi_df.groupby('Country', group_keys=False).apply(interpolate_mpi)

# --- 3. Merge with population dataset ---
# First ensure data types match
mpi_interpolated['Year'] = mpi_interpolated['Year'].astype(int)
pop_df['Year'] = pop_df['Year'].astype(int)

# Merge on Country and Year
merged = pd.merge(pop_df, mpi_interpolated, on=['Country', 'Year'])

# Rename columns for clarity
merged = merged.rename(columns={
    'Country Code': 'Code',
    'Population_Density': 'Pop_Density',
    'Value': 'MPI_Value'
})

# --- 4. Final output ---
final = merged[['Country', 'Code', 'Year', 'Pop_Density', 'MPI_Value']]
final.to_csv("merged_mpi_pop_density.csv", index=False)
print("✅ Merged data saved: merged_mpi_pop_density.csv")
