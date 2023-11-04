from dash import Dash, dcc, html 
from dash.dependencies import Input, Output
from . import ids
from src.data.loader import load_insta_data


def current_metric(data, metric) -> float: 

    current_metric = data[metric].iloc[-1]
    return current_metric


def metric_compare_week(data, metric) -> str: 

    add_metric = data[metric].iloc[-1] - data[metric].iloc[-2]

    if add_metric < 0: 
        symbol = '-'
    else: 
        symbol = '+'

    return f'{symbol} {abs(add_metric)} compared to last week'




