import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Load merged dataset
df = pd.read_csv('cleaned_population_density_mpi_no_singapore.csv')

# Load country centroids (ensure columns: Country_Code, Latitude, Longitude)
centroids = pd.read_csv('country_centroids.csv')

# Merge to include coordinates
df = df.merge(centroids, left_on='Code', right_on='Country_Code', how='left')

# Filter valid years and remove rows with missing or zero data
df = df[df['Year'].between(2008, 2024)].dropna(subset=['Population Density', 'MPI'])
df = df[df['Population Density'] > 0].copy()

# Calculate MPI / Population Density ratio
df['Ratio'] = df['MPI'] / df['Population Density']

# Flag top 10 countries with highest ratio per year
df['Top10Ratio'] = False
for yr, grp in df.groupby('Year'):
    top10_codes = grp.sort_values('Ratio', ascending=False).head(10)['Code']
    df.loc[(df['Year'] == yr) & (df['Code'].isin(top10_codes)), 'Top10Ratio'] = True

# Legend label for highlight
highlight_legend = 'Top 10 MPI / Density'

# Unique years for animation
years = sorted(df['Year'].unique())

# Create frames per year
frames = []
for year in years:
    d = df[df['Year'] == year]
    highlight = d[d['Top10Ratio']]

    choropleth = go.Choropleth(
        locations=d['Code'],
        z=d['MPI'],
        colorscale='YlOrBr',
        zmin=0,
        zmax=df['MPI'].max(),
        colorbar=dict(title='MPI'),
        text=d['Country'],
        hovertemplate='<b>%{text}</b><br>MPI: %{z:.3f}<br>'
                      'Pop Density: %{customdata[0]:.1f}<br>'
                      'Ratio: %{customdata[1]:.4f}<extra></extra>',
        customdata=np.stack([d['Population Density'], d['Ratio']], axis=-1),
        name='MPI'
    )

    scatter = go.Scattergeo(
        lon=highlight['Longitude'],
        lat=highlight['Latitude'],
        mode='markers',
        marker=dict(
            size=11,
            color='black',
            opacity=0.95,
            line=dict(width=2, color='yellow'),
            symbol='circle'
        ),
        text=highlight['Country'],
        hoverinfo='text',
        name=highlight_legend,
    )

    frames.append(go.Frame(data=[choropleth, scatter], name=str(year)))

# Initial frame (first year)
d0 = df[df['Year'] == years[0]]
init_choropleth = go.Choropleth(
    locations=d0['Code'],
    z=d0['MPI'],
    colorscale='YlOrBr',
    zmin=0,
    zmax=df['MPI'].max(),
    colorbar=dict(title='<b>MPI</b>'),
    text=d0['Country'],
    hovertemplate='<b>%{text}</b><br>MPI: %{z:.3f}<br>'
                  'Pop Density: %{customdata[0]:.1f}<br>'
                  'Ratio: %{customdata[1]:.4f}<extra></extra>',
    customdata=np.stack([d0['Population Density'], d0['Ratio']], axis=-1),
    name='MPI'
)

init_scatter = go.Scattergeo(
    lon=d0[d0['Top10Ratio']]['Longitude'],
    lat=d0[d0['Top10Ratio']]['Latitude'],
    mode='markers',
    marker=dict(
        size=11,
        color='black',
        opacity=0.95,
        line=dict(width=2, color='yellow'),
        symbol='circle'
    ),
    text=d0[d0['Top10Ratio']]['Country'],
    hoverinfo='text',
    name=highlight_legend,
)

# Final animated figure
fig = go.Figure(
    data=[init_choropleth, init_scatter],
    frames=frames,
    layout=go.Layout(
        title='<b>Low Density and High MPI Regions Highlight (2008–2024)</b>',
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

# Add annotation for black markers
fig.update_layout(
    annotations=[
        dict(
            text="<b>⚫ Black dots : Top 10 countries with highest MPI / Population Density ratio (low density + high MPI)</b>",
            xref='paper', yref='paper',
            x=0, y=-0.27,
            showarrow=False,
            font=dict(size=12),
            align='left'
        )
    ]
)

# Export to HTML
fig.write_html('choropleth_mpi_density_ratio_top10.html', auto_open=True)
print("✅ Map saved as 'choropleth_mpi_density_ratio_top10.html'")