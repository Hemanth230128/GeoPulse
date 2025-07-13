import pandas as pd

# -------- 1. Load files ------------------------------------------------------
mpi = pd.read_csv("mpi_interpolated.csv")          # Contains: Country,Country Code,Year,Value
pop = pd.read_csv("population_density.csv")        # Contains: Country,Country Code,Year,Population,Land_Area,Population_Density

# -------- 2. Rename 'Country Code' to 'Country_Code' for consistency --------
mpi = mpi.rename(columns={'Country Code': 'Country_Code'})
pop = pop.rename(columns={'Country Code': 'Country_Code'})

# -------- 3. Select only needed columns -------------------------------------
mpi = mpi[['Country_Code', 'Year', 'Value']]  # Don't include 'Country' yet to avoid conflict
pop = pop[['Country', 'Country_Code', 'Year', 'Population_Density']]

# -------- 4. Merge on Country_Code and Year ---------------------------------
merged = pd.merge(pop, mpi, on=['Country_Code', 'Year'], how='inner')

# -------- 5. Final formatting ------------------------------------------------
merged = merged.rename(columns={
    'Population_Density': 'Pop_Density',
    'Value': 'MPI'
})

# Rearrange columns
merged = merged[['Country', 'Country_Code', 'Year', 'Pop_Density', 'MPI']]

# ✅ Keep only from 2005 onwards
merged = merged[merged['Year'] >= 2005].reset_index(drop=True)

# -------- 6. Save result -----------------------------------------------------
merged.to_csv("merged_mpi_pop_density.csv", index=False)
print("✅ Merge successful! Sample output:")
print(merged.head())
