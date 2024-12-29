from fuzzywuzzy import process
import pandas as pd

df_queries = pd.read_csv('functions/InsightBot/user_queries.csv')

def user_query_mapping(query):

    '''
    Return the answer most closely associated with the user's query.

    This function takes the user's query, matches it against a database of answered queries, 
    and then returns the answered query most similar to the user's query. 

    The algorithm currently in use is fuzzy matching. Currently outputs the string with 
    the highest score, if the threshold is above 80 it'll output the string 
    associated to it. 

    query: The question or query asked by the user.

    Return: The response associated with the matched query or a default 
            message if no match is found.

    Example:
    query = "What is the highest number of followers?"

    df_queries['QUERIES'] -> holds all the strings 
      
    similarity_score = process.extractOne(query, df_queries['QUERY'])[1]
    --> 86

    highest_match = process.extractOne(query, df_queries['QUERY'])[0]
    --> 'The week starting from 09/10/2022 had the highest number of followers, with a total of 9676.'

    matches = process.extract(query, df_queries['QUERY'])
    --> Gets all the matches

    '''

    query = query.lower()

    similarity_score = process.extractOne(query, df_queries['QUERY'])[1]
    highest_match = process.extractOne(query, df_queries['QUERY'])[0]

    # matches = process.extract(query, df_queries['QUERY'])

    if similarity_score > 80:
        return highest_match
    else: 
        return "Unclear question"