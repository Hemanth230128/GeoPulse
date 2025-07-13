import pandas as pd
import plotly.graph_objects as go

# Load your data
df = pd.read_json('../data/merged/final_merged_data.json')

# Filter to years 2000-2022
df = df[(df['Year'] >= 2000) & (df['Year'] <= 2022)]

# Get list of countries
countries = sorted(df['Country'].unique())

# Default country
default_country = 'India' 

# Prepare traces for a given country
def make_traces(country):
    d = df[df['Country'] == country].sort_values('Year')
    years = d['Year']

    trace_gdp = go.Scatter(x=years, y=d['GDP Growth (%)'], mode='lines+markers', name='<b>GDP Growth (%)</b>')
    trace_mal = go.Scatter(x=years, y=d['Malnutrition Rate'], mode='lines+markers', name='<b>Malnutrition Rate (%)</b>')
    trace_lit = go.Scatter(x=years, y=d['Literacy Rate'], mode='lines+markers', name='<b>Literacy Rate (%)</b>')

    return [trace_gdp, trace_mal, trace_lit]

# Initial traces for default country
data = make_traces(default_country)

# Create frames for all countries
frames = []
for country in countries:
    frames.append(go.Frame(data=make_traces(country), name=country))

# Dropdown menu for selecting country
dropdown = dict(
    buttons=[
        dict(
            label=country,
            method="animate",
            args=[[country],
                  {"frame": {"duration": 500, "redraw": True},
                   "mode": "immediate",
                   "transition": {"duration": 300}}]
        ) for country in countries
    ],
    direction="down",
    x=1.01,
    y=0.85,
    showactive=True,
    xanchor="left",
    yanchor="top",
    pad={"r": 10, "t": 10},
    type="dropdown"
)

# Play and Pause buttons
play_pause_buttons = [
    dict(
        type="buttons",
        direction="left",
        x=0.1,
        y=-0.1,
        showactive=False,
        buttons=[
            dict(
                label="<b>Play</b>",
                method="animate",
                args=[None, 
                      {"frame": {"duration": 1000, "redraw": True},
                       "fromcurrent": True,
                       "transition": {"duration": 500},
                       "mode": "immediate"}]
            ),
            dict(
                label="<b>Pause</b>",
                method="animate",
                args=[[None], 
                      {"frame": {"duration": 0, "redraw": False},
                       "mode": "immediate",
                       "transition": {"duration": 0}}]
            )
        ],
        pad={"r": 10, "t": 10}
    )
]

layout = go.Layout(
    title=f" <b>GDP Growth, Malnutrition, Literacy Rate (2000-2022)</b>",
    xaxis=dict(title='<b>Year</b>', range=[2000, 2023]),
    yaxis=dict(title='<b>Value</b>', autorange=True),
    updatemenus=[dropdown] + play_pause_buttons,
    height=730,
    margin=dict(l=80, r=150, b=80, t=100)
)

fig = go.Figure(data=data, layout=layout, frames=frames)

fig.write_html("../outputs/country_line_chart.html", auto_open=True)
print("Line chart saved as 'country_line_chart.html'")
