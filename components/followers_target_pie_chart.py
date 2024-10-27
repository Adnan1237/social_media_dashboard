import plotly.express as px 
from dash import Dash, dcc, html
# from . import ids
# from . import metrics_item_structure
# from . import eng_metrics_predictions
from . import loader

sc_data = loader.load_insta_data()
# sc_data = eng_metrics_predictions.eng_pred_model(sc_data)

follower_data = loader.load_follower_data()

def render(app: Dash) -> html.Div:

    fig = px.pie(
            follower_data, 
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
            x=0.5, y=0.55,
            font=dict(size=20),
            showarrow=False
        ),

        dict(
            text="JAN 2024 TARGET",
            x=0.5, y=0.42,  # Adjust the y-coordinate for positioning
            font=dict(size=12),  # Use a smaller font size
            showarrow=False
        )
    ]
    
    fig.update_traces(textinfo='none')

    fig.update_layout(showlegend=False, 
                      margin=dict(l=0, r=0, t=0, b=0), 
                      height=None, 
                      width=None, 
                      annotations=annotations    
    )
    
    chart_layout = html.Div(
                        dcc.Graph(
                            figure=fig, 
                            style={'height': '100%', 'width': '100%'},
                        ), 
                        style={'height': '100%', 'width': '100%', 'overflow': 'hidden'}
                   )
    
    return chart_layout