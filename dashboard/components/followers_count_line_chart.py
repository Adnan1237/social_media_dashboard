import pandas as pd
import plotly.express as px 
from dash import Dash, dcc, html
from dash.dependencies import Input, Output 
from . import ids
from dashboard.data.loader import load_insta_data

SC_DATA_PATH = 'datasets/sc_social_media_master.csv'

sc_data = load_insta_data(SC_DATA_PATH)

def render(app: Dash) -> html.Div:

    fig = px.line(sc_data, 
                  x='DATE', 
                  y='followers_stand', 
                  text='followers_stand', 
                  color_discrete_sequence=['#92d051'], 
                )

    fig.update_layout(
        height=480, 
        width=1150, 
        margin={'l': 15, 'r': 105},
        xaxis_title='',
        yaxis_title='', 
        title='<b>Follower Count per Week<b>', 
        title_font=dict(size=20),
        title_x=0.5, 
        plot_bgcolor='rgba(0,0,0,0)', 
    )


    fig.update_traces(
        text=None, 
        line=dict(width=5),
    )

    for trace in fig.data:
        for x_val, y_val in zip(trace.x, trace.y):
            annotation_text=f'<b>{y_val}<b>'
            fig.add_annotation(
                x=x_val,
                y=y_val, 
                text=annotation_text,
                showarrow=False,
                font=dict(size=14, color='black'),
                # xshift=16 if trace.name == 'Instagram' else -16,
                yshift=15
            )
    
    return html.Div(dcc.Graph(figure=fig, 
                    config={'displayModeBar': False}, 
                    id=ids.F_LINE_CHART), 
                    style={'align': 'center', 'height': '450px', 'width': '1305px'}) 
