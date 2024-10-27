import pandas as pd
import math

def eng_pred_model(df, model='moving_avg'):

    eng_metrics = ['impressions', 'reach']
    if model=='moving_avg': 
        
        window_size = 3
        for metric in eng_metrics:
            df[f'{metric}_{model}'] = df[metric].rolling(window=window_size).mean()
            df[f'{metric}_{model}_pred_actual_diff'] = ((df[metric] - df[f'{metric}_{model}']) / df[metric]) * 100

            df[f'{metric}_{model}_pred_actual_diff'] = df[f'{metric}_{model}_pred_actual_diff'].apply(lambda x: 0 if math.isnan(x) or math.isinf(x) else int(round(x)))

    return df