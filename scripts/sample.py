import pandas as pd
import plotly.graph_objects as go

# Load your data
df = pd.read_json('../data/merged/final_merged_data.json')

# Choose size column
size_col = 'Child Population Density' if 'Child Population Density' in df.columns else 'Population Density'

# Drop missing data
df = df.dropna(subset=['GDP Growth (%)', 'Malnutrition Rate', size_col, 'Literacy Rate'])

years = sorted(df['Year'].unique())

frames = []

for year in years:
    d = df[df['Year'] == year]
    condition = (d['GDP Growth (%)'] > 4) & (d['Malnutrition Rate'] > 25)
    
    base_scatter = go.Scatter(
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
        colorbar=dict(
        title=dict(
            text='Literacy Rate (%)',
            side='top',           # Can be 'top', 'bottom', 'right'
            font=dict(size=14)      # Optional: title font size
        ),
            x=1.05,
           
            y=0.45,
            len=0.7,  # bigger colorbar
            thickness=20
        ),
        line=dict(width=0)
    ),
    text=d['Country'],
    hovertemplate=(
        '%{text}<br>GDP Growth: %{x:.2f}%<br>'
        'Malnutrition: %{y:.2f}%<br>'
        'Literacy: %{marker.color:.1f}%<br>'
        f'Child Pop Density: %{{marker.size:.1f}}<extra></extra>'
    ),
    name='All countries'
)

    
    ring_scatter = go.Scatter(
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
    
    frames.append(go.Frame(data=[base_scatter, ring_scatter], name=str(year)))

# Initial data: first year
initial_data = frames[0].data

ffig = go.Figure(
    data=initial_data,
    layout=go.Layout(
        title=f'<b>Malnutrition vs GDP Growth</b>',
        xaxis=dict(
            title='<b>GDP Growth (%)</b>',
            range=[df['GDP Growth (%)'].min(), df['GDP Growth (%)'].max()],
            zeroline=False
        ),
        yaxis=dict(
            title='<b>Malnutrition Rate (%)</b>',
            range=[0, df['Malnutrition Rate'].max()],
            zeroline=False
        ),
        height=750,  # Increased height for better spacing
        margin=dict(l=30, r=120, b=150, t=80),  # Larger bottom and right margins
        updatemenus=[
            dict(
                type='buttons',
                showactive=False,
                y=-0.05,
                x=1,
                xanchor='right',
                yanchor='top',
                buttons=[
                    dict(
                        label='<b>Play</b>',
                        method='animate',
                        args=[
                            None,
                            {
                                "frame": {"duration": 500, "redraw": True},
                                "fromcurrent": True,
                                "transition": {"duration": 300}
                            }
                        ]
                    ),
                    dict(
                        label='<b>Pause</b>',
                        method='animate',
                        args=[
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                                "transition": {"duration": 0}
                            }
                        ]
                    )
                ]
            )
        ],
        sliders=[
            dict(
                active=0,
                currentvalue={"prefix": "Year: "},
                pad={"b": 50, "t": 30},
                x=0.1,
                len=0.8,
                steps=[
                    dict(
                        method='animate',
                        args=[
                            [str(year)],
                            {
                                "mode": "immediate",
                                "frame": {"duration": 300, "redraw": True},
                                "transition": {"duration": 300}
                            }
                        ],
                        label=f"<b>{str(year)}</b>"
                    ) for year in years
                ]
            )
        ],
        annotations=[
            dict(
                text=(
                    f"<b>Bubble size:</b> child population density; <b>Bubble color:</b> Literacy Rate (%)<br>"
                    f"<b>Countries outlined in red</b> have GDP Growth > 4% and Malnutrition Rate > 25%."
                ),
                showarrow=False,
                xref='paper',
                yref='paper',
                x=0,
                y=-0.3,  # Below plot area
                align='left',
                font=dict(size=12)
            )
        ]
    ),
    frames=frames
)



# Save to html file and open automatically
ffig.write_html('../outputs/bubble_chart.html', auto_open=True)
print("Bubble chart saved as 'bubble_chart.html'")
