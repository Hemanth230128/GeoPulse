import pandas as pd

df = pd.read_csv('../data/raw/child_pop_india.csv')

# Keep only the required columns and rename them
df = df[['TIME_PERIOD:Time period', 'OBS_VALUE:Observation Value']].rename(columns={
    'TIME_PERIOD:Time period': 'Year',
    'OBS_VALUE:Observation Value': 'ChildPop'
})

df['ChildPopGrowth'] = df['ChildPop'].pct_change()

df = df.dropna().reset_index(drop=True)
df.to_csv('../data/cleaned/child_pop_growth_india.csv', index=False)
