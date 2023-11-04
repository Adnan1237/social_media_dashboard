import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output 
from . import ids
from data.loader import load_insta_data

SC_DATA_PATH = './datasets/sc_social_media_master.csv'

sc_data = load_insta_data(SC_DATA_PATH)

def render(app: Dash) -> html.Div:

    area_trace1 = go.Scatter(
        x=sc_data['DATE'],
        y=sc_data['impressions_reach'],
        fill='tozeroy',
        line=dict(color='#EEAA79'),
        fillcolor='#EEAA79', 
        name='Impressions', 
        showlegend=False
    )

    area_trace2 = go.Scatter(
        x=sc_data['DATE'],
        y=sc_data['accounts_reached'],
        fill='tozeroy',
        line=dict(color='#3CAADA'),
        fillcolor='#3CAADA', 
        name='Reach', 
        showlegend=False
    )

    fig = go.Figure()
    fig.add_trace(area_trace1)
    fig.add_trace(area_trace2)
    
    fig.update_layout(
        height=350, 
        width=650, 
        margin={'l': 0, 'r': 70, 't': 50},
        title="<b><span style='color:#EEAA79;'>Impressions</span> & <span style='color:#3CAADA;'>Reach</span> per Week<b>", 
        xaxis_title='',
        yaxis_title='', 
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig.update_traces(
        text=None, 
        line=dict(width=5),
    )
    
    return html.Div(dcc.Graph(figure=fig, 
                    config={'displayModeBar': False}, 
                    id=ids.IR_LINE_CHART), 
                    style={'align': 'center', 'height': '500px', 'width': '600px'}) 
