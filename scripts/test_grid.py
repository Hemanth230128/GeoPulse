import pyvista as pv
import numpy as np

grid = pv.UniformGrid()

# Configure the grid
grid.dimensions = (10, 10, 10)
grid.spacing = (1, 1, 1)
grid.origin = (0, 0, 0)

# Add random scalar data
grid["scalars"] = np.random.rand(1000)

# Save it
grid.save("test.vti")
print("Saved test.vti")
