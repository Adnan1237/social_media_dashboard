import pandas as pd
import plotly.express as px 
from dash import Dash, dcc, html
from dash.dependencies import Input, Output 
from . import ids
from . import loader

sc_data = loader.load_gender_split_data()

def render(app: Dash) -> html.Div:

    fig = px.pie(sc_data, 
                 values='PERCENTAGE', 
                 names='GENDER', 
                 color='GENDER',
                 color_discrete_map={'Male': '#ffd966', 'Female': '#92d051'}, 
          )

    fig.update_layout(
        height=None, 
        width=None, 
        xaxis_title=None, 
        yaxis_title=None, 
        margin=dict(l=0, r=0, t=0, b=0), 
        legend=dict(
            title="",
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1,
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

    chart_layout = html.Div(
                        children=[
                            dcc.Graph(
                                figure=fig, 
                                style={'height': '100%', 'width': '100%'},
                            )
                        ], 
                        style={'height': '100%', 'width': '100%', 'overflow': 'hidden'}
                   )

    return chart_layout  
            
            
