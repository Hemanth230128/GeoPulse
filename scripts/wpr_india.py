import pandas as pd

df = pd.read_csv('WPR.csv')

# Keep only the required columns and rename them
df = df[['Year', 'Value']].rename(columns={
    'Value': 'WPR'
})

df.to_csv('wpr_india.csv', index=False)
