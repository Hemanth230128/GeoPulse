'''
import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import plotly.express as px
import json
from shapely.geometry import shape

# Load data
df = pd.read_csv("dist_pred_all.csv")
df['District'] = df['District'].str.strip().str.lower()

with open("map.geojson") as f:
    geojson = json.load(f)

# Normalize GeoJSON district names
for feature in geojson["features"]:
    feature["properties"]["DISTRICT"] = feature["properties"]["DISTRICT"].strip().lower()

# Compute centroids for each district
centroids = {}
for feature in geojson["features"]:
    name = feature["properties"]["DISTRICT"]
    try:
        geom = shape(feature["geometry"])
        centroid = geom.centroid
        centroids[name] = {"lat": centroid.y, "lon": centroid.x}
    except:
        centroids[name] = {"lat": 22.97, "lon": 78.65}

# Risk stats
q_low = df['Risk_Factor'].quantile(0.05)
q_high = df['Risk_Factor'].quantile(0.95)

# Get year range
years = sorted(df['Year'].unique())

# App setup
app = dash.Dash(__name__)
app.title = "District Risk Visualizer"

app.layout = html.Div([
    html.H3("District-Level Poverty/Malnutrition Risk (2025–2030)", style={"textAlign": "center"}),

    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id="year-dropdown",
            options=[{"label": str(y), "value": y} for y in years],
            value=2025,
            clearable=False,
            style={"width": "200px"}
        )
    ], style={"textAlign": "center", "marginBottom": "10px"}),

    dcc.Graph(id="map", config={"displayModeBar": False}),
    dcc.Store(id='clicked-district', data=None),

    html.Button("Reset View", id="reset-btn", n_clicks=0,
                style={"margin": "10px auto", "display": "block"}),

    html.Div(id="district-info", style={
        "position": "fixed", "top": "100px", "right": "50px",
        "width": "300px", "backgroundColor": "white",
        "border": "2px solid #888", "borderRadius": "10px",
        "padding": "18px", "boxShadow": "0 2px 10px #88888880",
        "display": "none", "zIndex": 15
    })
])

@app.callback(
    Output("map", "figure"),
    Output("district-info", "style"),
    Output("district-info", "children"),
    Output("clicked-district", "data"),
    Input("map", "clickData"),
    Input("reset-btn", "n_clicks"),
    Input("year-dropdown", "value"),
    State("clicked-district", "data")
)
def update_map(click_data, reset_clicks, selected_year, stored_district):
    ctx = dash.callback_context
    triggered = ctx.triggered[0]["prop_id"].split(".")[0] if ctx.triggered else None

    # Filter data for selected year
    dff = df[df['Year'] == selected_year]

    # Default view
    zoom = 4
    center = {"lat": 22.9734, "lon": 78.6569}
    selected = None
    info_style = {"display": "none"}
    info_content = []

    # Clicked district logic
    if triggered == "map" and click_data:
        selected = click_data["points"][0]["location"]
        center = centroids.get(selected, center)
        zoom = 7
        row = dff[dff["District"] == selected].iloc[0]
        info_style = {"display": "block"}
        info_content = [
            html.H4(row["District"].title()),
            html.P(f"Risk Factor: {row['Risk_Factor']:.3f}"),
            html.P(f"Child Population Growth: {row['Child_Population_Growth']:.3f}"),
            html.P(f"Literacy: {row['Literacy']:.2f}%"),
            html.P(f"WPR: {row['WPR']:.2f}%")
        ]
    elif triggered == "reset-btn":
        selected = None

    # Adjust opacity to simulate "blur"
    opacities = {}
    for district in dff["District"]:
        opacities[district] = 0.85 if selected is None or district == selected else 0.2

    fig = px.choropleth_map(
        dff,
        geojson=geojson,
        locations="District",
        featureidkey="properties.DISTRICT",
        color="Risk_Factor",
        color_continuous_scale="YlOrRd",
        range_color=(q_low, q_high),
        map_style="carto-positron",
        zoom=zoom,
        center=center,
        opacity=0.9,
        hover_name="District",
        hover_data=["Risk_Factor"]
    )
    fig.update_traces(marker={"opacity": [opacities.get(loc, 0.85) for loc in dff["District"]]})
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=800)

    return fig, info_style, info_content, selected

if __name__ == "__main__":
    app.run(debug=True)
'''

import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import plotly.express as px
import json
from shapely.geometry import shape

from district_to_state import district_to_state

# --- Load Data ---
DATA_PATH = '../data/merged/district_forecast_2025_2030_all_fields.csv'
GEO_PATH = '../data/merged/map.geojson'
df = pd.read_csv(DATA_PATH)
with open(GEO_PATH, 'r') as f:
    geojson = json.load(f)

df['District'] = df['District'].str.strip().str.lower()

district_to_state_lower = {k.strip().lower(): v for k, v in district_to_state.items()}
df['State'] = df['District'].map(district_to_state_lower)

for feature in geojson["features"]:
    feature["properties"]["DISTRICT"] = feature["properties"]["DISTRICT"].strip().lower()

# --- Compute Centroids ---
centroids = {}
for feature in geojson["features"]:
    name = feature["properties"]["DISTRICT"]
    try:
        geom = shape(feature["geometry"])
        centroid = geom.centroid
        centroids[name] = {"lat": centroid.y, "lon": centroid.x}
    except:
        centroids[name] = {"lat": 22.97, "lon": 78.65}

# --- Global Values ---
q_low = df['Risk_Factor'].quantile(0.05)
q_high = df['Risk_Factor'].quantile(0.95)
years = sorted(df['Year'].unique())
default_center = {"lat": 22.9734, "lon": 78.6569}

# --- Dash App ---
app = dash.Dash(__name__)
app.title = "District Risk Visualizer"

app.layout = html.Div([
    html.H3("District-Level Poverty/Malnutrition Risk (2025–2030)", style={"textAlign": "center"}),

    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id="year-dropdown",
            options=[{"label": str(y), "value": y} for y in years],
            value=2025,
            clearable=False,
            style={"width": "200px"}
        )
    ], style={"textAlign": "center", "marginBottom": "10px"}),
    dcc.Graph(
        id='map',
        style={'height': '80vh', 'width': '100%', 'padding': '0', 'margin': '0'},
        config={"displayModeBar": False}
    ),
    dcc.Store(id='clicked-district', data=None),

    html.Button("Reset View", id="reset-btn", n_clicks=0,
                style={"margin": "10px auto", "display": "block"}),

    html.Div(id="district-info", style={
        "position": "fixed", "top": "100px", "right": "50px",
        "width": "300px", "backgroundColor": "white",
        "border": "2px solid #888", "borderRadius": "10px",
        "padding": "18px", "boxShadow": "0 2px 10px #88888880",
        "display": "none", "zIndex": 15
    })
], style={'height': '100vh', 'margin': '0', 'padding': '0'})

@app.callback(
    Output("map", "figure"),
    Output("district-info", "style"),
    Output("district-info", "children"),
    Output("clicked-district", "data"),
    Input("map", "clickData"),
    Input("reset-btn", "n_clicks"),
    Input("year-dropdown", "value"),
    State("clicked-district", "data")
)
def update_map(click_data, reset_clicks, selected_year, stored_district):
    ctx = dash.callback_context
    triggered = ctx.triggered[0]["prop_id"].split(".")[0] if ctx.triggered else None

    # Filter current year
    dff = df[df['Year'] == selected_year]

    # Defaults
    zoom = 4
    center = default_center
    info_style = {"display": "none"}
    info_content = []
    new_selected = None

    if triggered == "reset-btn":
        pass  # Just reset to full view

    elif triggered == "map" and click_data:
        clicked = click_data["points"][0]["location"]

        # If clicking same district again: toggle off
        if stored_district == clicked:
            new_selected = None
        else:
            new_selected = clicked
            center = centroids.get(clicked, default_center)
            zoom = 7

            # Info box
            try:
                row = dff[dff["District"] == clicked].iloc[0]
                info_style = {"display": "block"}
                info_content = [
                    html.H4(row["District"].title()),
                    html.P(f"Risk Factor: {row['Risk_Factor']:.3f}"),
                    html.P(f"Child Population Growth: {row['Child_Population_Growth']:.3f}"),
                    html.P(f"Literacy: {row['Literacy']:.2f}%"),
                    html.P(f"WPR: {row['WPR']:.2f}%")
                ]
            except:
                info_style = {"display": "none"}
                info_content = []

    elif stored_district:
        # Re-apply previous district state (e.g., year dropdown change)
        new_selected = stored_district
        center = centroids.get(stored_district, default_center)
        zoom = 7
        try:
            row = dff[dff["District"] == stored_district].iloc[0]
            info_style = {"display": "block"}
            info_content = [
                html.H4(row["District"].title()),
                html.P(f"Risk Factor: {row['Risk_Factor']:.3f}"),
                html.P(f"Child Population Growth: {row['Child_Population_Growth']:.3f}"),
                html.P(f"Literacy: {row['Literacy']:.2f}%"),
                html.P(f"WPR: {row['WPR']:.2f}%")
            ]
        except:
            info_style = {"display": "none"}

    # Build opacity map
    opacities = {}
    for district in dff["District"]:
        opacities[district] = 0.85 if new_selected is None or district == new_selected else 0.2

    fig = px.choropleth_map(
        dff,
        geojson=geojson,
        locations="District",
        featureidkey="properties.DISTRICT",
        color="Risk_Factor",
        color_continuous_scale="YlOrRd",
        range_color=(q_low, q_high),
        map_style="carto-positron",
        zoom=zoom,
        center=center,
        opacity=0.9,
        hover_name="District",
        hover_data=["Risk_Factor"]
    )
    fig.update_traces(marker={"opacity": [opacities.get(loc, 0.85) for loc in dff["District"]]})
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=800)

    return fig, info_style, info_content, new_selected

if __name__ == "__main__":
    app.run(debug=True, port=8051)
