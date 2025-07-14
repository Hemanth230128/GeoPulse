import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv("mpinew.csv")

# Average duplicates
df = df.groupby(['Country', 'Year'], as_index=False)['Value'].mean()

# Final output
all_rows = []

for country, group in df.groupby("Country"):
    group = group.sort_values("Year").reset_index(drop=True)
    
    known_years = group['Year'].values
    known_values = group['Value'].values

    # Full range of years between first and last
    full_years = np.arange(known_years.min(), known_years.max() + 1)
    
    # Create DataFrame with all years in range
    temp_df = pd.DataFrame({
        'Country': country,
        'Year': full_years
    })
    
    # Map known values
    temp_df['Value'] = temp_df['Year'].map(dict(zip(known_years, known_values)))

    # Interpolate missing years (only inside range)
    temp_df['Value'] = temp_df['Value'].interpolate(method='linear', limit_area='inside')

    all_rows.append(temp_df)

# Combine all
final_df = pd.concat(all_rows, ignore_index=True)

# Save result
final_df.to_csv("mpi_interpolated.csv", index=False)
print("✅ Done! Missing years (within known range) are interpolated.")
