import pandas as pd
import json
import plotly.express as px 
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output 
from . import ids
from components.metrics_item_structure import metrics_item_structure
from components.eng_metrics_predictions import eng_pred_model
from . import loader

sc_data = loader.load_insta_data()
sc_data = eng_pred_model(sc_data)

def render(app: Dash) -> html.Div:

    area_trace1 = go.Scatter(
        x=sc_data['DATE'],
        y=sc_data['impressions'],
        fill='tozeroy',
        line=dict(color='#EEAA79'),
        fillcolor='#EEAA79', 
        name='Impressions', 
        showlegend=False
    )

    area_trace2 = go.Scatter(
        x=sc_data['DATE'],
        y=sc_data['reach'],
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
    )
    
    # chart_layout =  html.Div([
    #                     html.Div(
    #                         html.Div(id='hover-info-ir')
    #                     ), 
    #                     html.Div(
    #                         dcc.Graph(
    #                             figure=fig, 
    #                             config={'displayModeBar': False}, 
    #                             id=ids.IR_LINE_CHART,
    #                         style={'height': '100%', 'width': '100%'},
    #                         )
    #                     )
    #                 ], style={'height': '100%', 'width': '100%', 'overflow': 'hidden'})

    chart_layout = html.Div(
                        dcc.Graph(
                            figure=fig, 
                            style={'height': '100%', 'width': '100%'},
                        ), 
                        style={'height': '100%', 'width': '100%', 'overflow': 'hidden'}
                   )

    
    # @app.callback(
    #     Output('hover-info-ir', 'children'), 
    #     [Input(ids.IR_LINE_CHART, 'hoverData')]
    # )

    # def update_hover_info(hover_data):
    #     if hover_data is not None:

    #         x_date = json.dumps(hover_data['points'][0]['x'])
    #         x_date = x_date.strip('""')

    #         input_date = pd.to_datetime(x_date, format='%Y-%m-%d')

    #         sc_data_subset = sc_data[sc_data['DATE'] == input_date]

    #         imp_act = sc_data_subset['impressions_reach'].iloc[0]
    #         reach_act = sc_data_subset['accounts_reached'].iloc[0]

    #         imp_act_pred_diff = sc_data_subset['impressions_reach_moving_avg_pred_actual_diff'].iloc[0]
    #         reach_act_pred_diff = sc_data_subset['accounts_reached_moving_avg_pred_actual_diff'].iloc[0]

    #         metric_layout = html.Div([
    #                             metrics_item_structure('impressions', imp_act, imp_act_pred_diff), 
    #                             metrics_item_structure('reach', reach_act, reach_act_pred_diff), 
    #                         ], style={'display': 'block', 'vertical-align': 'top'})

    #         return metric_layout
        
    #     else: 
    #         max_date = sc_data['DATE'].max()
    #         sc_data_subset = sc_data[sc_data['DATE'] == max_date]

    #         imp_act = sc_data_subset['impressions_reach'].iloc[0]
    #         reach_act = sc_data_subset['accounts_reached'].iloc[0]

    #         imp_act_pred_diff = sc_data_subset['impressions_reach_moving_avg_pred_actual_diff'].iloc[0]
    #         reach_act_pred_diff = sc_data_subset['accounts_reached_moving_avg_pred_actual_diff'].iloc[0]            
            
    #         metric_layout_max_date = html.Div([
    #                                     metrics_item_structure('impressions', imp_act, imp_act_pred_diff), 
    #                                     metrics_item_structure('reach', reach_act, reach_act_pred_diff), 
    #                                 ], style={'display': 'block', 'vertical-align': 'top'})


    #     return metric_layout_max_date

    return chart_layout
                   