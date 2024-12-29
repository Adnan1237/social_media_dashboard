from dash import Dash, html 
from . import followers_target_pie_chart
from . import followers_age_bar_chart
from . import followers_gender_pie_chart
from . import followers_count_line_chart
from . import impressions_reach_line_chart
from . import engagement_score_line_chart
from components.metrics_item_structure import metrics_item_structure

def create_layout(app: Dash) -> html.Div:

    return html.Div(
        className="parent-container",
        children=[
            html.Div(
                className="container",
                children=[
                    html.Div(
                        className='demographic-section', 
                        children=[
                            html.Div(followers_target_pie_chart.render(app), className="box", id="pie-target"),
                            html.Div(followers_gender_pie_chart.render(app), className="box", id="pie-gender"), 
                            html.Div(followers_age_bar_chart.render(app), className="box", id="bar-age")
                        ]
                    ),
                    html.Div(
                        id="insightbot"
                    ),
                    html.Div(
                        className="imp-reach-section", 
                        id="box-d", 
                        children=[
                            html.Div(metrics_item_structure('impressions'), id="box-d1"), 
                            html.Div(metrics_item_structure('reach'), id="box-d2"), 
                            html.Div(impressions_reach_line_chart.render(app), id="box-d3"), 
                        ]
                    ), 
                    html.Div(followers_count_line_chart.render(app), className="box", id="box-e"),
                    html.Div(
                        className="eng-section", 
                        id="box-f", 
                        children=[
                            html.Div(metrics_item_structure('likes'), id="box-f1"), 
                            html.Div(metrics_item_structure('comments'), id="box-f2"), 
                            html.Div(metrics_item_structure('saves'), id="box-f3"), 
                            html.Div(metrics_item_structure('shares'), id="box-f4"),
                            html.Div("F5", id="box-f5"),
                        ]
                    ),  
                    html.Div("G", className="box", id="box-g")
                ]
            )
        ]
    )