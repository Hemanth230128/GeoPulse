import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Input data
data = {
    'Year': [2002, 2006, 2012, 2022],
    'Literacy': [0.61, 0.68, 0.74, 0.81] #reference:internet
}

df = pd.DataFrame(data).set_index('Year')

# Interpolate from 2000 to 2022
df_interp = df.reindex(range(2000, 2023))
df_interp['Literacy'] = df_interp['Literacy'].interpolate(method='linear', limit_direction='both')*100
df_interp = df_interp.dropna(subset=['Literacy'])

# Combine and save
df_interp = df_interp.reset_index().rename(columns={'index': 'Year'})
df_interp.to_csv("../data/cleaned/literacy_india.csv", index=False)
print(df_interp)
