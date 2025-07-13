# -------- Feature 1: year_and_risk_app.py --------
# Displays India-wide map with year and risk score filters

import pandas as pd
import plotly.express as px
import json
from dash import Dash, dcc, html, Input, Output
from district_to_state import district_to_state

# Load data
DATA_PATH = '../data/merged/district_forecast_2025_2030_all_fields.csv'
GEO_PATH = '../data/merged/map.geojson'
df = pd.read_csv(DATA_PATH)
with open(GEO_PATH, 'r') as f:
    geojson = json.load(f)

# Normalize district names
df['Year'] = df['Year'].astype(int)
df['District'] = df['District'].str.strip().str.lower()
for feature in geojson['features']:
    feature['properties']['district'] = feature['properties']['DISTRICT'].strip().lower()

# State mapping
district_to_state_lower = {k.strip().lower(): v for k, v in district_to_state.items()}
district_to_state_lower.update({
    'andaman islands': 'Andaman & Nicobar Island',
    'barabanki': 'Uttar Pradesh',
    'leh (ladakh)': 'Jammu and Kashmir',
    'mumbai (suburban)': 'Maharashtra',
    'ri bhoi': 'Meghalaya',
    'sant ravidas nagar bhadohi': 'Uttar Pradesh',
    'senapati': 'Manipur',
    'south  twenty four parganas': 'West Bengal',
})
df['State'] = df['District'].map(district_to_state_lower)

# Slider values
years = sorted(df['Year'].unique())
risk_min = float(df['Risk_Factor'].min())
risk_max = float(df['Risk_Factor'].max())
q_low = df['Risk_Factor'].quantile(0.05)
q_high = df['Risk_Factor'].quantile(0.95)

# App 1
app1 = Dash(__name__)
app1.layout = html.Div([
    html.H2("India Risk Map (Year & Risk Filter)"),
    dcc.Slider(
        id='year-slider',
        min=int(min(years)), max=int(max(years)), step=1,
        value=int(min(years)),
        marks={int(y): str(int(y)) for y in years}
    ),
    dcc.RangeSlider(
        id='risk-slider',
        min=risk_min, max=risk_max, step=0.01,
        value=[risk_min, risk_max],
        marks={float(v): str(round(v, 2)) for v in df['Risk_Factor'].quantile([0, 0.25, 0.5, 0.75, 1]).tolist()}
    ),
    dcc.Graph(
        id='map1',
        style={'height': '80vh', 'width': '100%', 'padding': '0', 'margin': '0'}
    )
], style={'height': '100vh', 'margin': '0', 'padding': '0'})

@app1.callback(
    Output('map1', 'figure'),
    Input('year-slider', 'value'),
    Input('risk-slider', 'value')
)
def update_map1(year, risk_range):
    dff = df[(df['Year'] == year) & (df['Risk_Factor'] >= risk_range[0]) & (df['Risk_Factor'] <= risk_range[1])]
    fig = px.choropleth_map(
        dff,
        geojson=geojson,
        locations='District',
        featureidkey='properties.district',
        color='Risk_Factor',
        color_continuous_scale='YlOrRd',
        map_style='carto-positron',
        zoom=4,
        center={'lat': 22.9734, 'lon': 78.6569},
        opacity=0.9,
        hover_name='District',
        hover_data=['State', 'Risk_Factor'],
        range_color=(q_low, q_high)
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

if __name__ == '__main__':
    app1.run(debug=False, port=8051)
