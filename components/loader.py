import pandas as pd
from datetime import datetime

# sheet_id = '1v8mQC4NW_DvMxpRf0NcRxP39SHSqdZHLYruSDX81WzE'

data = 'data/master.csv'
target_follower_data = {'TARGET_MONTH': ['JAN_2023'], 'FOLLOWERS_TARGET': [1500]}

def load_insta_data() -> pd.DataFrame: 

    data = 'data/master.csv'

    sc_data = pd.read_csv(
        data
    )

    date_format = "%d/%m/%Y"

    # sc_data['START_DATE'] = [datetime.strptime(start, date_format) for start in sc_data['START_DATE']]
    # sc_data['END_DATE'] = [datetime.strptime(end, date_format) for end in sc_data['END_DATE']]
    sc_data['DATE'] = [datetime.strptime(date, date_format) for date in sc_data['week_start_date']]

    return sc_data 


def load_follower_data(target_dt = 'JAN_2023') -> pd.DataFrame:

    sc_data = load_insta_data()

    follower_data = pd.DataFrame(
        target_follower_data
    )

    current_followers = sc_data['followers'].iloc[-1]

    follower_data['FOLLOWERS_TARGET_PCT'] = [(current_followers / followers) * 100 for followers in follower_data['FOLLOWERS_TARGET']]
    follower_data['EMPTY_PCT'] = 100 - follower_data['FOLLOWERS_TARGET_PCT'] 

    follower_data_melt = pd.melt(follower_data, id_vars=['TARGET_MONTH', 'FOLLOWERS_TARGET'], 
                                 var_name='labels', value_name='values')
    
    follower_data_melt = follower_data_melt[follower_data_melt['TARGET_MONTH'] == target_dt][['labels', 'values']]
    follower_data_melt['values'] = follower_data_melt['values'].round().astype(int)

    # pie_data = {'labels': ['FOLLOWERS_TARGET_PCT', 'EMPTY_PCT'],
    #             'values': [38.4, 61]}

    return follower_data_melt


def load_age_split_data() -> pd.DataFrame: 
    
    data = 'data/master.csv'

    sc_data = pd.read_csv(
        data
    )
   
    sc_data_age_avg = sc_data[['1317_followers', '1824_followers', '2534_followers', 
                               '3544_followers', '4554_followers', '5564_followers', 
                               '65plus_followers']].mean().reset_index()
    
    sc_data_age_avg = sc_data_age_avg.rename(columns={'index': 'AGE', 0: 'Sacred Compass'})
    sc_data_age_avg['Instagram'] = [8, 31, 3, 16, 8, 4, 0]

    sc_data_age_avg['AGE'] = sc_data_age_avg['AGE'].replace({'1317_followers': '13-17', 
                                                             '1824_followers': '18-24',
                                                             '2534_followers': '25-34',
                                                             '3544_followers': '35-44',
                                                             '4554_followers': '45-54',
                                                             '5564_followers': '55-64',
                                                             '65plus_followers': '65 +'})
    
    # sc_data_age_avg[['Sacred Compass', 'Instagram']] = sc_data_age_avg[['Sacred Compass', 'Instagram']] * 100
    sc_data_age_avg[['Sacred Compass', 'Instagram']] = sc_data_age_avg[['Sacred Compass', 'Instagram']].round().astype(int)

    sc_data_age_avg = sc_data_age_avg.melt(id_vars='AGE', var_name='CHANNEL', value_name='PERCENTAGE')

    return sc_data_age_avg


def load_gender_split_data() -> pd.DataFrame: 
   
    data = 'data/master.csv'

    sc_data = pd.read_csv(
        data
    )

    sc_data_gender_avg = sc_data[['male_followers', 'female_followers']].mean().reset_index()
    sc_data_gender_avg = sc_data_gender_avg.rename(columns={'index': 'GENDER', 0: 'PERCENTAGE'})

    sc_data_gender_avg['GENDER'] = sc_data_gender_avg['GENDER'].replace({'male_followers': 'Male', 
                                                                         'female_followers': 'Female'})
    
    sc_data_gender_avg['PERCENTAGE'] = sc_data_gender_avg['PERCENTAGE'] * 100
    sc_data_gender_avg['PERCENTAGE'] = sc_data_gender_avg['PERCENTAGE'].round().astype(int)

    return sc_data_gender_avg