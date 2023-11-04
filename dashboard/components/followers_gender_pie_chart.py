import pandas as pd
import plotly.express as px 
from dash import Dash, dcc, html
from dash.dependencies import Input, Output 
from . import ids
from dashboard.data.loader import load_gender_split_data

sc_data = load_gender_split_data()

def render(app: Dash) -> html.Div:

    fig = px.pie(sc_data, 
                 values='PERCENTAGE', 
                 names='GENDER', 
                 color='GENDER',
                 color_discrete_map={'Male': '#ffd966', 'Female': '#92d051'}, 
          )

    fig.update_layout(
        height=350, 
        width=300, 
        xaxis_title=None, 
        yaxis_title=None, 
        margin={'l': 0, 'r': 50},
        legend=dict(
          title="",
          orientation="h",
          yanchor="bottom",
          y=1.05,
          xanchor="right",
          x=0.83,
          font=dict(size=15)
        ),
      plot_bgcolor='rgba(0,0,0,0)'
    )
    
    fig.update_traces(
        textinfo='percent',
        texttemplate='<br><b>%{percent:.0%}</b>',  # Use <b> tag for bold
        insidetextfont=dict(size=20), 
        pull=[0.02, 0.02]
    )

    return html.Div(
                    children=[
                            dcc.Graph(
                                figure=fig, 
                                config={'displayModeBar': False}, 
                                id=ids.G_PIE_CHART, 
                                style={'height': '300px', 'width': '400px', 'overflow': 'hidden'} 
                            ) 
                    ]    
                )  
            
            
