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

    chart_layout =  html.Div([
                        html.Div(
                            html.Div(id='hover-info')
                        ), 
                        html.Div([
                            html.Div(
                                dcc.Graph(
                                    # figure=fig, 
                                    config={'displayModeBar': False}, 
                                    id=ids.ENG_SCORE_LINE_CHART, 
                                    style={'height': '100%', 'width': '100%'}
                                )
                            ), 
                            html.Div([
                                dcc.Input(
                                    id=f'user_weight_{weight}',
                                    type='number',
                                    placeholder = f'insert weight: {weight}',
                                    debounce=True,  # Changes are only made to the dash app if you press enter 
                                    style={'height': '100%', 'width': '100%', 'overflow': 'hidden'}
                                ) for weight in eng_types
                            ])
                        ], style={'display': 'flex', 'verticalAlign': 'top'})
                    ], style={'display': 'block', 'verticalAlign': 'top'})
    
    
    @app.callback(
        Output(ids.ENG_SCORE_LINE_CHART, 'figure'), 
        [Input(f'user_weight_{weight}', 'value')
         for weight in eng_types]
    )

    def update_eng_score_line_chart(user_weight_likes, user_weight_comments, user_weight_shares, user_weight_saves):

        user_weight_likes = user_weight_likes or 0.1 # If user_weight_likes empty, give 0.1 as weighting 
        user_weight_comments = user_weight_comments or 0.35
        user_weight_shares = user_weight_shares or 0.45
        user_weight_saves = user_weight_saves or 0.1

        weight_likes = user_weight_likes
        weight_comments = user_weight_comments
        weight_shares = user_weight_shares
        weight_saves = user_weight_saves

        sc_data['eng_composite_score'] = (
            weight_likes * sc_data['norm_likes'] + 
            weight_comments * sc_data['norm_comments'] + 
            weight_shares * sc_data['norm_shares'] + 
            weight_saves * sc_data['norm_saves']
        )

        print('Weighting of Likes: ' + str(user_weight_likes))
        print('Weighting of Comments: ' + str(user_weight_comments))
        print('Weighting of Shares: ' + str(user_weight_shares))
        print('Weighting of Saves: ' + str(user_weight_saves))

        fig = px.line(sc_data, 
                  x='week_start_date', 
                  y='eng_composite_score', 
                  color_discrete_sequence=['#92d051'], 
                )

        # fig.update_layout(
        #     height=370, 
        #     width=840, 
        #     margin={'l': 15, 'r': 15, 'b': 10},
        #     xaxis_title='',
        #     yaxis_title='', 
        #     title='<b>Engagement Score per Week<b>', 
        #     title_font=dict(size=20),
        #     title_x=0.5, 
        #     plot_bgcolor='rgba(0,0,0,0)', 
        # )

        fig.update_layout(
            height=None, 
            width=None, 
            margin=dict(l=0, r=0, t=0, b=0), 
            # title="<b><span style='color:#EEAA79;'>Impressions</span> & <span style='color:#3CAADA;'>Reach</span> per Week<b>", 
            xaxis_title='',
            yaxis_title='', 
            plot_bgcolor='rgba(0,0,0,0)'
        )


        fig.update_traces(
            text=None, 
            line=dict(width=5),
            hovertemplate='Engagement Score: %{y:.2f}'
        )

        return fig
    
    @app.callback(
        Output('hover-info', 'children'), 
        [Input(ids.ENG_SCORE_LINE_CHART, 'hoverData')]
    )

    def update_hover_info(hover_data):
        if hover_data is not None:

            x_date = json.dumps(hover_data['points'][0]['x'])
            x_date = x_date.strip('""')

            input_date = pd.to_datetime(x_date, format='%Y-%m-%d')

            sc_data_subset = sc_data[sc_data['DATE'] == input_date]

            likes_act = sc_data_subset['likes'].iloc[0]
            comments_act = sc_data_subset['comments'].iloc[0]
            saves_act = sc_data_subset['saves'].iloc[0]
            shares_act = sc_data_subset['shares'].iloc[0]

            likes_pred = sc_data_subset['likes_moving_avg_pred_actual_diff'].iloc[0]
            comments_pred = sc_data_subset['comments_moving_avg_pred_actual_diff'].iloc[0]
            saves_pred = sc_data_subset['saves_moving_avg_pred_actual_diff'].iloc[0]
            shares_pred = sc_data_subset['shares_moving_avg_pred_actual_diff'].iloc[0]

            metric_layout = html.Div([
                                metrics_item_structure('likes', likes_act, likes_pred), 
                                metrics_item_structure('comments', comments_act, comments_pred), 
                                metrics_item_structure('shares', shares_act, shares_pred), 
                                metrics_item_structure('saves', saves_act, saves_pred), 
                            ], style={'display': 'block', 'vertical-align': 'top'})

            return metric_layout
        
        else: 
            max_date = sc_data['DATE'].max()
            sc_data_subset = sc_data[sc_data['DATE'] == max_date]

            likes_act = sc_data_subset['likes'].iloc[0]
            comments_act = sc_data_subset['comments'].iloc[0]
            saves_act = sc_data_subset['saves'].iloc[0]
            shares_act = sc_data_subset['shares'].iloc[0]

            likes_pred = sc_data_subset['likes_moving_avg_pred_actual_diff'].iloc[0]
            comments_pred = sc_data_subset['comments_moving_avg_pred_actual_diff'].iloc[0]
            saves_pred = sc_data_subset['saves_moving_avg_pred_actual_diff'].iloc[0]
            shares_pred = sc_data_subset['shares_moving_avg_pred_actual_diff'].iloc[0]

            metric_layout_max_date = html.Div([
                                        metrics_item_structure('likes', likes_act, likes_pred), 
                                        metrics_item_structure('comments', comments_act, comments_pred), 
                                        metrics_item_structure('shares', shares_act, shares_pred), 
                                        metrics_item_structure('saves', saves_act, saves_pred), 
                                    ], style={'display': 'block', 'vertical-align': 'top'})

        return metric_layout_max_date

    return chart_layout
