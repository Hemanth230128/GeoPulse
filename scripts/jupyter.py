import pandas as pd
import plotly.graph_objects as go
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML

# ── 1. Load and Clean ─────────────────────────────────────────────
df = pd.read_json('../data/merged/final_merged_data.json')

# Use Child Population Density if available
if 'Child Population Density' in df.columns:
    size_col = 'Child Population Density'
else:
    size_col = 'Population Density'

# Drop rows with missing data
df = df.dropna(subset=['GDP Growth (%)', 'Malnutrition Rate', size_col, 'Literacy Rate'])

# ── 2. Create Year Slider ─────────────────────────────────────────
year_slider = widgets.IntSlider(
    value=int(df['Year'].max()),
    min=int(df['Year'].min()),
    max=int(df['Year'].max()),
    step=1,
    description='<b>Year:</b>',
    continuous_update=False
)

output = widgets.Output()

# ── 3. Plotting Function ──────────────────────────────────────────
def draw_bubble(year):
    d = df[df['Year'] == year].copy()
    if d.empty:
        with output:
            clear_output(wait=True)
            print(f'No data for year {year}')
        return
    
    # Condition for red outline
    condition = (d['GDP Growth (%)'] > 4) & (d['Malnutrition Rate'] > 25)
    
    base = go.Scatter(
        x=d['GDP Growth (%)'],
        y=d['Malnutrition Rate'],
        mode='markers',
        marker=dict(
            size=d[size_col],
            sizemode='area',
            sizeref=2.*d[size_col].max() / (60**2),
            color=d['Literacy Rate'],
            colorscale='Viridis',
            showscale=True,
            line=dict(width=0)
        ),
        text=d['Country'],
        hovertemplate=
            '%{text}<br>GDP Growth: %{x:.2f}%<br>'
            'Malnutrition: %{y:.2f}%<br>'
            'Literacy: %{marker.color:.1f}%<br>'
            f'{size_col}: %{{marker.size:.1f}}<extra></extra>',
        name='All countries'
    )
    
    ring = go.Scatter(
        x=d[condition]['GDP Growth (%)'],
        y=d[condition]['Malnutrition Rate'],
        mode='markers',
        marker=dict(
            size=d[condition][size_col],
            sizemode='area',
            sizeref=2.*d[size_col].max() / (60**2),
            color='rgba(0,0,0,0)',
            line=dict(width=2, color='red')
        ),
        text=d[condition]['Country'],
        hoverinfo='skip',
        showlegend=False
    )
    
    fig = go.Figure([base, ring])
    fig.update_layout(
        title=f'<b>Malnutrition vs GDP Growth – {year}</b>',
        xaxis_title='<b>GDP Growth (%)</b>',
        yaxis_title='<b>Malnutrition Rate (%)</b>',
        height=600
    )
    
    with output:
        clear_output(wait=True)
        fig.show()
        display(HTML(
            f"<b>Selected Year:</b> {year}<br>"
            f"<b>Bubble size:</b> {size_col}<br>"
            f"<b>Bubble color:</b> Literacy Rate (%)<br>"
            f"<b>Red outline:</b> Countries with GDP > 4% and Malnutrition > 25%"
        ))

# ── 4. Initial Plot ───────────────────────────────────────────────
draw_bubble(year_slider.value)

# ── 5. Slider-Plot Binding ────────────────────────────────────────
def on_slider_change(change):
    if change['name'] == 'value':
        draw_bubble(change['new'])

year_slider.observe(on_slider_change, names='value')

# ── 6. Display UI ─────────────────────────────────────────────────
display(year_slider, output)
