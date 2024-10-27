import pandas as pd
import plotly.express as px 
from dash import Dash, dcc, html
from . import loader

sc_data = loader.load_insta_data()

def render(app: Dash) -> html.Div:

    fig = px.line(sc_data, 
                  x='DATE', 
                  y='followers', 
                  text='followers', 
                  color_discrete_sequence=['#92d051'], 
                )

    fig.update_layout(
        height=None, 
        width=None, 
        margin=dict(l=0, r=0, t=0, b=0), 
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

    fig.update_xaxes(tickformat="%b %Y")

    for trace in fig.data:
        for x_val, y_val in zip(trace.x, trace.y):
            annotation_text=f'<b>{y_val}<b>'
            fig.add_annotation(
                x=x_val,
                y=y_val, 
                text=annotation_text,
                showarrow=False,
                font=dict(size=10, color='black'),
                # xshift=16 if trace.name == 'Instagram' else -16,
                yshift=15
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
