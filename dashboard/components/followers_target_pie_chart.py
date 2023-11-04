import pandas as pd
import plotly.express as px 
from dash import Dash, dcc, html
from dash.dependencies import Input, Output 
from . import ids
from dashboard.data.loader import load_insta_data, load_follower_data

SC_DATA_PATH = r'C:\Users\adnan\OneDrive\Documents\dashboard_projects\social_media_dashboard\datasets\sc_social_media_master.csv'
TARGET_DATA_PATH = SC_DATA_PATH = r'C:\Users\adnan\OneDrive\Documents\dashboard_projects\social_media_dashboard\datasets\followers_target.csv'

sc_data = load_insta_data(SC_DATA_PATH)
follower_data = load_follower_data(TARGET_DATA_PATH, sc_data)

def render(app: Dash) -> html.Div:

    fig = px.pie(follower_data, 
                 values='values', 
                 names='labels', 
                 hole=0.65, 
                 color='labels', 
                 color_discrete_map={'FOLLOWERS_TARGET_PCT': '#92d051', 'EMPTY_PCT': '#ededed'}, 
                )

    followers_target_pct = follower_data.loc[follower_data['labels'] == 'FOLLOWERS_TARGET_PCT', 'values'].iloc[0]

    annotations = [
    dict(
        text=f"<b>{followers_target_pct}%<b>",
        x=0.5, y=0.7,
        font=dict(size=15),
        showarrow=False
    ),
    dict(
        text="JAN 2024 TARGET",
        x=0.5, y=0.42,  # Adjust the y-coordinate for positioning
        font=dict(size=7),  # Use a smaller font size
        showarrow=False
    )]
    
    fig.update_traces(textinfo='none')

    fig.update_layout(showlegend=False, 
                      margin=dict(l=0, r=0, t=0, b=0), 
                      height=100, 
                      width=200, 
                      annotations=annotations    
    )
    
    return html.Div(dcc.Graph(figure=fig), 
                    id=ids.F_PIE_CHART, 
                    style={'height': '100px'}
            )
            