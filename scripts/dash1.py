import pandas as pd
import plotly.express as px
import json
import dash
from dash import Dash, dcc, html, Input, Output, State
from shapely.geometry import shape
from district_to_state import district_to_state
import os


# --- Load Data ---
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/merged/district_forecast_2025_2030_all_fields.csv'))
GEO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/merged/map.geojson'))
df = pd.read_csv(DATA_PATH)
with open(GEO_PATH, 'r') as f:
    geojson = json.load(f)

# --- Normalize District Names ---
df['Year'] = df['Year'].astype(int)
df['District'] = df['District'].str.strip().str.lower()
for feature in geojson['features']:
    feature['properties']['district'] = feature['properties']['DISTRICT'].strip().lower()

# --- State Mapping ---
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

# --- Compute Centroids ---
centroids = {}
for feature in geojson["features"]:
    name = feature["properties"]["district"]
    try:
        geom = shape(feature["geometry"])
        centroid = geom.centroid
        centroids[name] = {"lat": centroid.y, "lon": centroid.x}
    except:
        centroids[name] = {"lat": 22.97, "lon": 78.65}

# --- Global Constants ---
years = sorted(df['Year'].unique())
risk_min = float(df['Risk_Factor'].min())
risk_max = float(df['Risk_Factor'].max())
q_low = df['Risk_Factor'].quantile(0.05)
q_high = df['Risk_Factor'].quantile(0.95)
default_center = {"lat": 22.9734, "lon": 78.6569}
print(risk_min,risk_max)
# --- Dash App ---
app = Dash(__name__)
app.title = "India Risk Map"
app.layout = html.Div([
    html.H2("India Risk Map (Year & Risk Filter)"),
    
    html.Div([
    html.Div("Year:", style={"width": "15%", "paddingRight": "10px", "fontWeight": "bold", "textAlign": "right"}),
    html.Div(
        dcc.Slider(
            id='year-slider',
            min=int(min(years)), max=int(max(years)), step=1,
            value=int(min(years)),
            marks={int(y): str(int(y)) for y in years}
        ),
        style={"width": "85%"}
    )
    ], style={"display": "flex", "alignItems": "center", "padding": "10px 30px"}),

    html.Div([
        html.Div("Risk Factor:", style={"width": "15%", "paddingRight": "10px", "fontWeight": "bold", "textAlign": "right"}),
        html.Div(
            dcc.RangeSlider(
                id='risk-slider',
                min=risk_min,
                max=risk_max + 0.01,
                step=0.01,
                value=[risk_min, risk_max + 0.01],
                marks={float(v): str(round(v, 2)) for v in df['Risk_Factor'].quantile([0, 0.25, 0.5, 0.75, 1]).tolist()}
            ),
            style={"width": "85%"}
        )
    ], style={"display": "flex", "alignItems": "center", "padding": "10px 30px"}),


    dcc.Graph(id='map1', style={'height': '80vh', 'width': '100%', 'padding': '0', 'margin': '0'}),
    
    html.Div([
        html.Button("Reset View", id="reset-btn", n_clicks=0, style={
            "margin": "10px auto",
            "padding": "10px 20px",
            "borderRadius": "8px",
            "border": "1px solid #ccc",
            "backgroundColor": "#f4f4f4",
            "cursor": "pointer",
            "fontWeight": "bold"
        })
    ], style={"textAlign": "center"}),
    
    dcc.Store(id='clicked-district', data=None),
    
    html.Div(id="district-info", style={
        "position": "absolute",
        "top": "100px",
        "right": "40px",
        "backgroundColor": "white",
        "border": "1px solid #ccc",
        "borderRadius": "10px",
        "padding": "16px",
        "boxShadow": "0px 4px 8px rgba(0,0,0,0.2)",
        "display": "none",
        "zIndex": "1000",
        "width": "280px"
    })
], style={'height': '100vh', 'margin': '0', 'padding': '0'})

# --- Callback ---
@app.callback(
    Output("map1", "figure"),
    Output("district-info", "style"),
    Output("district-info", "children"),
    Output("clicked-district", "data"),
    Input("map1", "clickData"),
    Input("reset-btn", "n_clicks"),
    Input("year-slider", "value"),
    Input("risk-slider", "value"),
    State("clicked-district", "data")
)
def update_map(click_data, reset_clicks, selected_year, risk_range, stored_district):
    ctx = dash.callback_context
    triggered = ctx.triggered[0]["prop_id"].split(".")[0] if ctx.triggered else None

    # Filter data
    dff = df[(df['Year'] == selected_year) & (df['Risk_Factor'] >= risk_range[0]) & (df['Risk_Factor'] <= risk_range[1])]
    
    zoom = 4
    center = default_center
    info_style = {"display": "none"}
    info_content = []
    new_selected = None

    if triggered == "reset-btn":
        new_selected = None
        center = default_center
        zoom = 4
        info_style = {"display": "none"}
        info_content = []

    elif triggered == "map1" and click_data:
        clicked = click_data["points"][0]["location"]
        if stored_district == clicked:
            new_selected = None
        else:
            new_selected = clicked
            center = centroids.get(clicked, default_center)
            zoom = 7
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

    opacities = {d: (0.85 if new_selected is None or d == new_selected else 0.2) for d in dff["District"]}

    fig = px.choropleth_map(
        dff,
        geojson=geojson,
        locations="District",
        featureidkey="properties.district",
        color="Risk_Factor",
        color_continuous_scale="YlOrRd",
        range_color=(q_low, q_high),
        map_style="carto-positron",
        zoom=zoom,
        center=center,
        opacity=0.9,
        hover_name="District",
        hover_data=["State", "Risk_Factor"]
    )
    fig.update_traces(marker={"opacity": [opacities.get(loc, 0.85) for loc in dff["District"]]})
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig, info_style, info_content, new_selected

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8051)
