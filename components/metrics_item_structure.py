from dash import html
from . import loader

sc_data = loader.load_insta_data()

def current_metric(data, metric) -> float:
    '''
    Output the latest record for given metric
    E.g. Value of current sales 
    '''
    current_metric = data[metric].iloc[-1]
    return current_metric


def metric_compare_week(data, metric) -> str: 
    '''
    This returns the difference between the latest record for a given metric against the week before 
    E.g. Current sales - last week's sales 
    '''
    add_metric = data[metric].iloc[-1] - data[metric].iloc[-2]
    
    if add_metric < 0:
        symbol = '-'
    else: 
        symbol = '+'

    return f'{symbol} {abs(add_metric)} vs. last week'



def metrics_item_structure(metric):

    actual = current_metric(sc_data, metric)
    compare = metric_compare_week(sc_data, metric)

    return html.Div(
                style={'height': '100%', 'width': '100%', 'display': 'inline-block', 'text-align': 'center', 'margin-top': '15px'},
                children=[
                    html.Img(src=f'assets/{metric}.png', alt='image', width=35, height=35),
                    html.H2(metric.upper(), style={'margin-bottom': '2px', 'font-weight': '500', 'font-size': '20px', 'margin-top': '2px'}),
                    html.H2(actual, style={'align': 'center', 'font-weight': '800', 'font-size': '30px'}),
                    html.H2(compare, style={'align': 'center', 'color': 'lightgrey', 'font-size': '18px'})
                ]
            )
