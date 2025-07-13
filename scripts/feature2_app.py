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

# Normalize
df['District'] = df['District'].str.strip().str.lower()
df['Year'] = df['Year'].astype(int)
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

# App setup
states = sorted(df['State'].dropna().unique())
q_low = df['Risk_Factor'].quantile(0.05)
q_high = df['Risk_Factor'].quantile(0.95)

app2 = Dash(__name__)
app2.layout = html.Div([
    html.H2("State-specific Risk Map Viewer"),
    dcc.Dropdown(
        id='state-dropdown',
        options=[{'label': s, 'value': s} for s in states],
        placeholder="Select a State",
        clearable=True
    ),
    dcc.Graph(
        id='map2',
        style={'height': '90vh', 'width': '100%', 'padding': '0', 'margin': '0'}
    )
], style={'height': '100vh', 'margin': '0', 'padding': '0'})

@app2.callback(
    Output('map2', 'figure'),
    Input('state-dropdown', 'value')
)
def update_map2(selected_state):
    # If no state is selected — full India map
    if not selected_state:
        fig = px.choropleth_map(
            df,
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

    # Filter data and geojson for selected state
    dff = df[df['State'] == selected_state]
    district_set = set(dff['District'])

    # Calculate center of selected state
    latitudes = []
    longitudes = []

    for feature in geojson['features']:
        district_name = feature['properties']['district']
        if district_name in district_set:
            geom = feature['geometry']
            coords = []
            if geom['type'] == 'Polygon':
                coords = geom['coordinates'][0]
            elif geom['type'] == 'MultiPolygon':
                coords = geom['coordinates'][0][0]
            for lon, lat in coords:
                longitudes.append(lon)
                latitudes.append(lat)

    if latitudes and longitudes:
        center_lat = sum(latitudes) / len(latitudes)
        center_lon = sum(longitudes) / len(longitudes)
    else:
        center_lat, center_lon = 22.9734, 78.6569  # fallback

    fig = px.choropleth_map(
        dff,
        geojson=geojson,
        locations='District',
        featureidkey='properties.district',
        color='Risk_Factor',
        color_continuous_scale='YlOrRd',
        map_style='carto-positron',
        zoom=5,
        center={'lat': center_lat, 'lon': center_lon},
        opacity=0.9,
        hover_name='District',
        hover_data=['Risk_Factor'],
        range_color=(q_low, q_high)
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

if __name__ == '__main__':
    app2.run(debug=False, port=8052)
