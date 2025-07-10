import pandas as pd
import numpy as np
import pyvista as pv

# Load CSV
df = pd.read_csv("population_vs_poverty.csv")
df = df.dropna()
df["Year"] = df["Year"].astype(int)
df["Country"] = df["Country"].astype(str)

# Create index mapping
countries = sorted(df["Country"].unique())
country_to_index = {c: i for i, c in enumerate(countries)}
df["CountryIndex"] = df["Country"].map(country_to_index)

# Define grid shape
x_dim = len(countries)
y_dim = df["Year"].nunique()
z_dim = 1  # 2D scalar grid embedded in 3D space

# Scalar grid (X: country, Y: year)
scalar_field = np.full((x_dim, y_dim, z_dim), np.nan)
for _, row in df.iterrows():
    x = country_to_index[row["Country"]]
    y = row["Year"] - df["Year"].min()
    scalar_field[x, y, 0] = row["Share below $2.15 a day"]

# Fill NaN with 0 or interpolate later
scalar_field = np.nan_to_num(scalar_field)

# Create ImageData (Uniform Grid)
grid = pv.ImageData()
grid.dimensions = np.array(scalar_field.shape) + 1
grid.origin = (0, 0, 0)
grid.spacing = (1, 1, 1)

# Flatten in column-major order (VTK expects Fortran order)
grid.cell_data["poverty_rate"] = scalar_field.flatten(order="F")

# Save
grid.save("poverty_timeseries.vti")
print("✅ Saved poverty_timeseries.vti")
