import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Load merged dataset
df = pd.read_csv('merged_mpi_pop_density.csv')

# Load country centroids (ensure columns: Country_Code, Latitude, Longitude)
centroids = pd.read_csv('country_centroids.csv')

# Merge to include coordinates
df = df.merge(centroids, on='Country_Code', how='left')

# Filter years
df = df[df['Year'].between(2005, 2022)].dropna(subset=['Pop_Density', 'MPI'])

# Define thresholds
density_threshold = df['Pop_Density'].median()
mpi_threshold = df['MPI'].median()


df['Mismatch'] = (df['Pop_Density'] < density_threshold) & (df['MPI'] > mpi_threshold)
mismatch_legend = 'Low Density & High MPI'

# Unique years for animation
years = sorted(df['Year'].unique())

# Create frames per year
frames = []
for year in years:
    d = df[df['Year'] == year]
    mismatch_countries = d[d['Mismatch']]

    choropleth = go.Choropleth(
        locations=d['Country_Code'],
        z=d['MPI'],
        colorscale='Inferno',
        zmin=0,
        zmax=df['MPI'].max(),
        colorbar=dict(title='MPI'),
        text=d['Country'],
        hovertemplate='<b>%{text}</b><br>MPI: %{z:.3f}<extra></extra>',
        name='MPI'
    )

    scatter = go.Scattergeo(
        lon=mismatch_countries['Longitude'],
        lat=mismatch_countries['Latitude'],
        mode='markers',
        marker=dict(
            size=8,
            color='red',
            line=dict(width=1, color='darkred'),
            symbol='circle'
        ),
        text=mismatch_countries['Country'],
        hoverinfo='text',
        name=f'Mismatch: {mismatch_legend}',
    )

    frames.append(go.Frame(data=[choropleth, scatter], name=str(year)))

# Initial data for first year
d0 = df[df['Year'] == years[0]]
init_choropleth = go.Choropleth(
    locations=d0['Country_Code'],
    z=d0['MPI'],
    colorscale='Inferno',
    zmin=0,
    zmax=df['MPI'].max(),
    colorbar=dict(title='<b>MPI</b>'),
    text=d0['Country'],
    hovertemplate='<b>%{text}</b><br>MPI: %{z:.3f}<extra></extra>',
    name='MPI'
)

init_scatter = go.Scattergeo(
    lon=d0[d0['Mismatch']]['Longitude'],
    lat=d0[d0['Mismatch']]['Latitude'],
    mode='markers',
    marker=dict(size=6, color='red', line=dict(width=1, color='darkred'), symbol='circle'),
    text=d0[d0['Mismatch']]['Country'],
    hoverinfo='text',
    name=f'Mismatch: {mismatch_legend}',
)

# Final figure
fig = go.Figure(
    data=[init_choropleth, init_scatter],
    frames=frames,
    layout=go.Layout(
        title=f'<b>{mismatch_legend} Regions Highlight (2005–2022)</b>',
        geo=dict(
            showcoastlines=True,
            showland=True,
            projection_type='natural earth',
            showcountries=True,
            countrycolor='LightGray',
        ),
        updatemenus=[dict(
            type='buttons',
            showactive=False,
            y=-0.05,
            x=1.06,
            xanchor='right',
            yanchor='top',
            buttons=[
                dict(label='<b>Play</b>', method='animate',
                     args=[None, {"frame": {"duration": 600, "redraw": True}, "fromcurrent": True}]),
                dict(label='<b>Pause</b>', method='animate',
                     args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}])
            ]
        )],
        sliders=[dict(
            active=0,
            currentvalue={"prefix": "<b>Year: </b>"},
            pad={"b": 40},
            steps=[
                dict(method='animate', args=[[str(y)], {"mode": "immediate", "frame": {"duration": 300, "redraw": True}}], label=f"<b>{str(y)}</b>")
                for y in years
            ]
        )]
    )
)

# Export and open
fig.write_html('choropleth_mpi_mismatch.html', auto_open=True)
print("✅ Choropleth with mismatch highlights saved as 'choropleth_mpi_mismatch.html'")
