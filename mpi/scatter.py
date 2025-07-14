import pandas as pd
import plotly.graph_objects as go

# Load main dataset
df = pd.read_csv('cleaned_population_density_mpi_no_singapore.csv')

# Load continent-region mapping
continent_df = pd.read_csv('country_regions.csv')

# Merge datasets on Country Code
df = df.merge(continent_df, left_on='Code', right_on='Country_Code', how='left')

# Assign "Other" to countries with missing region mapping
df['Region_Name'] = df['Region_Name'].fillna('Other')

# 🎨 Map regions to colors
region_colors = {
    'South Asia': '#FF7F0E',
    'Europe & Central Asia': '#1F77B4',
    'Middle East & North Africa': '#D62728',
    'Sub-Saharan Africa': '#9467BD',
    'Latin America & Caribbean': '#2CA02C',
    'East Asia & Pacific': '#8C564B',
    'North America': '#E377C2',
    'Other': '#7F7F7F'  # Gray for unmapped
}

# Check for countries assigned to "Other"
other_countries = df[df['Region_Name'] == 'Other']['Country'].unique()
if len(other_countries) > 0:
    print("⚠️ Countries assigned to 'Other' (not found in country_regions.csv):")
    for country in other_countries:
        print("-", country)

# Drop rows with missing population density or MPI
df = df.dropna(subset=['Population Density', 'MPI'])

# Ensure years are sorted
years = sorted(df['Year'].unique())

# Prepare frames for each year
frames = []
for year in years:
    d = df[df['Year'] == year]

    scatter = go.Scatter(
        x=d['Population Density'],
        y=d['MPI'],
        mode='markers',
        marker=dict(
            size=12,
            color=d['Region_Name'].map(region_colors),  # ✅ Region color mapping
            line=dict(width=0.5, color='DarkSlateGrey'),
            symbol='circle'
        ),
        text=d['Country'],
        hovertemplate=(
            '%{text}<br>Region: %{customdata[0]}<br>'
            'Pop Density: %{x:.1f}<br>'
            'MPI: %{y:.3f}<extra></extra>'
        ),
        customdata=d[['Region_Name']],
        showlegend=False  # 🚨 Prevent automatic legend
    )

    frames.append(go.Frame(data=[scatter], name=str(year)))

# Initial data (first year)
initial_data = frames[0].data

# 🆕 Add dummy scatter traces for regions (for legend only)
legend_traces = []
for region, color in region_colors.items():
    legend_traces.append(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=12, color=color),
        name=region,
        showlegend=True
    ))

# Combine initial data with legend traces
full_initial_data = list(initial_data) + legend_traces

# Create figure with slider
fig = go.Figure(
    data=full_initial_data,
    layout=go.Layout(
        title='<b>Population Density vs MPI (2008–2024)</b>',
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
        margin=dict(l=30, r=220, t=80, b=80),  # 🆕 extra margin for legend
        legend=dict(
            title='<b>Regions</b>',
            traceorder='normal',
            x=1.05,
            y=1,
            font=dict(size=12)
        ),
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

# Save and show
fig.write_html("scatter_mpi_pop.html", auto_open=True)
print("✅ Scatter plot saved as 'scatter_mpi_pop.html'")
