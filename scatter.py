import pandas as pd
import plotly.graph_objects as go

# Load merged dataset
df = pd.read_csv('merged_mpi_pop_density.csv')

# Drop missing values
df = df.dropna(subset=['Pop_Density', 'MPI'])

# Ensure years are sorted
years = sorted(df['Year'].unique())

# Prepare frames for each year
frames = []
for year in years:
    d = df[df['Year'] == year]

    scatter = go.Scatter(
        x=d['Pop_Density'],
        y=d['MPI'],
        mode='markers',
        marker=dict(
            size=15,  # Uniform size for all markers
            color=d['MPI'],
            colorscale='Inferno',
            showscale=True,
            colorbar=dict(
                title="MPI",
                x=1.02,
                len=0.6,
                thickness=20
            ),
            line=dict(width=0.5, color='DarkSlateGrey')
        ),
        text=d['Country'],
        hovertemplate=(
            '%{text}<br>Pop Density: %{x:.1f}<br>'
            'MPI: %{y:.3f}<extra></extra>'
        ),
        name=''
    )

    frames.append(go.Frame(data=[scatter], name=str(year)))

# Initial data (first year)
initial_data = frames[0].data

# Create figure with slider
fig = go.Figure(
    data=initial_data,
    layout=go.Layout(
        title='<b>Population Density vs MPI (2005–2021)</b>',
        xaxis=dict(
            title='<b>Population Density</b>',
            type='log',
            zeroline=False
        ),
        yaxis=dict(
            title='<b>Multidimensional Poverty Index</b>',
            zeroline=False
        ),
        height=750,
        margin=dict(l=30, r=100, t=80, b=80),
        sliders=[dict(
            active=0,
            currentvalue={"prefix": "<b>Year: </b>"},
            pad={"b": 50},
            x=0.1,
            len=0.8,
            steps=[
                dict(
                    method='animate',
                    args=[[str(year)], {"frame": {"duration": 300, "redraw": True}, "mode": "immediate"}],
                    label=f"<b>{str(year)}</b>"
                ) for year in years
            ]
        )],
        updatemenus=[dict(
            type='buttons',
            showactive=False,
            x=1,
            y=-0.05,
            buttons=[
                dict(label='<b>Play</b>', method='animate',
                     args=[None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}]),
                dict(label='<b>Pause</b>', method='animate',
                     args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}])
            ]
        )],
    ),
    frames=frames
)
fig.update_layout(
    annotations=[
        dict(
            text="<b>Marker color</b> = MPI",
            xref='paper', yref='paper',
            x=0, y=-0.26,
            showarrow=False,
            align='left',
            font=dict(size=12)
        )
    ]
)

# Save and show
fig.write_html("scatter_mpi_pop.html", auto_open=True)
print("✅ Scatter plot saved as 'scatter_mpi_pop.html'")