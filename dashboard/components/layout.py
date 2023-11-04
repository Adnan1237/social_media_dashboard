from dash import Dash, html 
import dash_bootstrap_components as dbc
from . import followers_target_pie_chart
from . import followers_count_line_chart
from . import followers_age_bar_chart
from . import followers_gender_pie_chart
from . import impressions_reach_line_chart
from . import followers_engagement_chart
from dashboard.components.metrics_card import current_metric, metric_compare_week


def create_layout(app: Dash, data) -> html.Div: 
    return html.Div([
            html.Div([
                html.Div(
                    style={'display': 'inline-block', 'border': '2px solid black', 'padding': '20px', 'height': '300px', 'width': '250px', 'text-align': 'center', 'align-items': 'center', 'float': 'left', 'margin-right': '5px', 'margin-bottom': '5px'},
                    children=[
                        html.Div(style={'height': '15px'}),
                        html.H2('FOLLOWERS', style={'margin-bottom': '10px', 'align': 'center', 'font-weight': '500', 'font-size': '25px'}), 
                        html.H2(current_metric(data, 'followers_stand'), style={'margin-bottom': '10px', 'align': 'center', 'font-weight': '800', 'font-size': '35px'}),
                        html.H2(metric_compare_week(data, 'followers_stand'), style={'margin-bottom': '10px', 'align': 'center', 'color': 'lightgrey', 'font-size': '18px'}),
                        html.H2(followers_target_pie_chart.render(app), style={'margin-bottom': '10px', 'align': 'center'})
                    ],
                ),
                html.Div([
                    followers_age_bar_chart.render(app),
                    followers_gender_pie_chart.render(app)
                ], style={'border': '2px solid black', 'display': 'flex', 'height': '300px', 'width': '800px', 'float': 'left', 'margin-bottom': '10px', 'margin-left': '10px', 'overflow': 'hidden'}),

                html.Div([
                    followers_count_line_chart.render(app)
                ], style={'border': '2px solid black', 'height': '450px', 'width': '1065px', 'text-align': 'center', 'clear': 'both', 'overflow': 'hidden'})
            ]
            ), 

            html.Div([
                html.Div([
                    html.Div(
                        style={'display': 'inline-block', 'border': '2px solid black', 'padding': '20px', 'height': '300px', 'width': '300px', 'text-align': 'center', 'margin-left': '10px', 'margin-bottom': '5px'},
                        children=[
                            html.H2('IMPRESSIONS', style={'margin-bottom': '10px', 'align': 'center', 'font-weight': '500', 'font-size': '25px', 'color': '#EEAA79'}), 
                            html.H2(current_metric(data, 'impressions_reach'), style={'margin-bottom': '10px', 'align': 'center', 'font-weight': '800', 'font-size': '35px'}),
                            html.H2(metric_compare_week(data, 'impressions_reach'), style={'margin-bottom': '10px', 'align': 'center', 'color': 'lightgrey', 'font-size': '18px'}),
                            html.Hr(style={'backgroundColor': 'gray'}),
                            html.H2('REACH', style={'margin-bottom': '10px', 'align': 'center', 'font-weight': '500', 'font-size': '25px', 'color': '#3CAADA'}), 
                            html.H2(current_metric(data, 'accounts_reached'), style={'margin-bottom': '10px', 'align': 'center', 'font-weight': '800', 'font-size': '35px'}),
                            html.H2(metric_compare_week(data, 'accounts_reached'), style={'margin-bottom': '10px', 'align': 'center', 'color': 'lightgrey', 'font-size': '18px'}),
                        ]
                    ), 

                    html.Div([
                        impressions_reach_line_chart.render(app),
                    ], style={'border': '2px solid black', 'display': 'flex', 'height': '300px', 'width': '600px', 'float': 'left', 'margin-bottom': '10px', 'margin-left': '10px', 'margin-right': '10px', 'align': 'center', 'overflow': 'hidden'}),
                    
                ], style={'display': 'flex', 'verticalAlign': 'top'}
                ), 

                html.Div([
                    html.Div([
                        html.Div([
                            html.H4('TOTAL ENGAGEMENT', style={'margin-bottom': '10px', 'align': 'center', 'font-weight': '500', 'font-size': '25px'})
                        ]),
                        followers_engagement_chart.render(app, 'total_engagement')
                    ])
                ], style={'display': 'inline-block', 'border': '2px solid black', 'padding': '20px', 'height': '300px', 'width': '300px', 'text-align': 'center', 'margin-left': '10px', 'margin-bottom': '5px'}
                )
    ])

    ], style={'display': 'flex', 'verticalAlign': 'top'})

        

