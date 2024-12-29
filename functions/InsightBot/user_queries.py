import re
import pandas as pd

data = 'data/master.csv'
df = pd.read_csv(data)


def highest_metric(metric_name):
    '''
    Return the week with the highest value for a specificied metric (e.g. impressions, likes, comments etc)

    metric_name: Name of the metric to be used in the retun statement 

    Return: A string describing the week with the highest value for a given metric 
    '''

    highest_week = df.loc[df[metric_name].idxmax()]['week_start_date']

    highest_value = df[metric_name].max()

    return f'The week starting from {highest_week} had the highest number of {metric_name}, with a total of {highest_value}.'


def lowest_metric(metric_name):
    '''
    Return the week with the lowest value for a specificied metric (e.g. impressions, likes, comments etc)

    metric_name: Name of the metric to be used in the retun statement 

    Return: A string describing the week with the lowest value for a given metric 
    '''

    lowest_week = df.loc[df[metric_name].idxmin()]['week_start_date']

    lowest_value = df[metric_name].min()

    return f'The week starting from {lowest_week} had the lowest number of {metric_name}, with a total of {lowest_value}.'


def average_metric(metric_name):
    '''
    Return the average value for a specificied metric (e.g. impressions, likes, comments etc)

    metric_name: Name of the metric to be used in the retun statement 

    Return: A string describing the average value for a given metric 
    '''

    average_value = round(df[metric_name].mean())

    return f'The average number of {metric_name} per week is {average_value}.'


def user_queries_list_generate():

    metrics = ['followers', 'impressions', 'reach', 'additional_followers', 
               'likes', 'comments', 'shares', 'saves']
    
    metric_list = []
    for metric in metrics:
        metric_list.append(highest_metric(metric))
        metric_list.append(lowest_metric(metric))
        metric_list.append(average_metric(metric))

    query_numbers = [f'query_{i+1}' for i in range(len(metric_list))]

    df_query_list = pd.DataFrame({
        'QUERY_NUMBER': query_numbers, 
        'QUERY': metric_list
    })

    return df_query_list


if __name__ == "__main__":

    user_queries_list_generate().to_csv('functions/InsightBot/user_queries.csv', index=False)

    
    