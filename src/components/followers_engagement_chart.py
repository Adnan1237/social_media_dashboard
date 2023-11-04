import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import plotly.subplots as sp
from dash import Dash, dcc, html
from dash.dependencies import Input, Output 
from . import ids
from data.loader import load_insta_data

SC_DATA_PATH = './datasets/sc_social_media_master.csv'

sc_data = load_insta_data(SC_DATA_PATH)

def render(app: Dash, interaction_type) -> html.Div:

    sc_data['total_engagement'] = sc_data['total_likes'] + sc_data['total_comments'] + sc_data['total_saves'] + sc_data['total_shares']

    fig = px.area(sc_data, 
                  x='DATE', 
                  y=interaction_type, 
                #   mode='lines',
                  labels={'Likes_to_Reach_Ratio': 'Likes to Reach Ratio'},
          )
    
    fig.update_layout(
        height=200, 
        width=250, 
        # xaxis_title='',
        # yaxis_title='', 
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis={'visible': False},
        yaxis={'visible': False},
        margin={'t': 0, 'b': 0, 'l': 0, 'r': 0}, 
    )

    return html.Div(dcc.Graph(figure=fig, 
                    config={'displayModeBar': False}, 
                    id=ids.FE_LINE_CHART, 
                    style={'width': '100%', 'height': '100%','padding': '0', 'margin': '0', 'height': 'auto'}
                    )) 
