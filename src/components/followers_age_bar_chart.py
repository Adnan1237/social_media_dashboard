import pandas as pd
import plotly.express as px 
from dash import Dash, dcc, html
from dash.dependencies import Input, Output 
from . import ids
from data.loader import load_age_split_data

SC_DATA_PATH = './datasets/sc_social_media_master.csv'

sc_data = load_age_split_data(SC_DATA_PATH)

def render(app: Dash) -> html.Div:

    fig = px.bar(sc_data, 
                 x='AGE', 
                 y='PERCENTAGE', 
                 color='CHANNEL', 
                 barmode='group', 
                 color_discrete_map={'Sacred Compass': '#ffd966', 'Instagram': '#92d051'})

    fig.update_layout(height=350, 
                      width=600, 
                      xaxis_title=None, 
                      yaxis_title=None, 
                      margin={'l': 15, 'r': 105},
                      bargap=0.3,
                      bargroupgap=0.2,
                      legend=dict(
                        title="",
                        orientation="h",
                        yanchor="bottom",
                        y=1.05,
                        xanchor="right",
                        x=0.83, 
                        font=dict(size=15)
                      ),
                      plot_bgcolor='rgba(0,0,0,0)')
    
    fig.update_yaxes(showticklabels=False)

    for trace in fig.data:
        for x_val, y_val in zip(trace.x, trace.y):
            annotation_text=f'<b>{y_val}%<b>'
            fig.add_annotation(
                x=x_val,
                y=y_val, 
                text=annotation_text,
                showarrow=False,
                font=dict(size=12, color='black'),
                xshift=16 if trace.name == 'Instagram' else -16,
                yshift=8

            )

    return html.Div(
                children=[
                        dcc.Graph(
                            figure=fig, 
                            config={'displayModeBar': False}, 
                            id=ids.F_BAR_CHART, 
                            style={'height': '300px', 'width': '500px', 'overflow': 'hidden'} 
                        ) 
                ]    
            )  
            
