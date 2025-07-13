import pandas as pd

# Load your CSV
df = pd.read_csv("combined_2001_2011.csv")

# Normalize Literacy Rate
df["Literacy Rate"] = df["Literacy Rate"] / 100

# Save to a new CSV (or overwrite the original)
df.to_csv("combined_2001_2011.csv", index=False)
