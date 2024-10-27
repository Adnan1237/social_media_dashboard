import pandas as pd
import math
import json
from datetime import datetime
import plotly.express as px 
from dash import Dash, dcc, html
from dash.dependencies import Input, Output 
from . import ids
from components.metrics_item_structure import metrics_item_structure
# from components.metrics_card import current_metric, metric_compare_week
from components.eng_metrics_predictions import eng_pred_model
from . import loader

sc_data = loader.load_insta_data()
sc_data = eng_pred_model(sc_data)
eng_types = ['likes', 'comments', 'shares', 'saves']

def render(app: Dash) -> html.Div:

    sc_data['norm_likes'] = (sc_data['likes'] - sc_data['likes'].min()) / (sc_data['likes'].max() - sc_data['likes'].min())
    sc_data['norm_comments'] = (sc_data['comments'] - sc_data['comments'].min()) / (sc_data['comments'].max() - sc_data['comments'].min())
    sc_data['norm_saves'] = (sc_data['saves'] - sc_data['saves'].min()) / (sc_data['saves'].max() - sc_data['saves'].min())
    sc_data['norm_shares'] = (sc_data['shares'] - sc_data['shares'].min()) / (sc_data['shares'].max() - sc_data['shares'].min())

    likes_weight = 0.1 # If user_weight_likes empty, give 0.1 as weighting 
    comments_weight = 0.35
    shares_weight = 0.45
    saves_weight = 0.1

    sc_data['eng_composite_score'] = (
        likes_weight * sc_data['norm_likes'] + 
        comments_weight * sc_data['norm_comments'] + 
        shares_weight * sc_data['norm_shares'] + 
        saves_weight * sc_data['norm_saves']
    )

    fig = px.line(
            sc_data, 
            x='week_start_date', 
            y='eng_composite_score', 
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

    
