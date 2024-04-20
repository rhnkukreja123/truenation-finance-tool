import os
import requests
from itertools import islice
from functions.utils import (
    query_parser,
    query_parser_for_two_currencies
)

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')



def get_time_series_daily_function(user_query:str):

    stock_symbol=query_parser(user_query)

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}'

    r = requests.get(url)
    data = r.json()
    input_dict=data["Time Series (Daily)"]
    data= dict(islice(input_dict.items(), 10))

    return data

def get_quote_endpoint_function(user_query:str):
    
    stock_symbol=query_parser(user_query)
 
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    data = r.json()

    return data

def get_exchange_rate_function(user_query:str):

    currency_1, currency_2=query_parser_for_two_currencies(user_query)

    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_1}&to_currency={currency_2}&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    data = r.json()

    return data


def get_time_series_weekly_function(user_query:str):

    stock_symbol=query_parser(user_query)

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    data = r.json()
    input_dict=data["Weekly Time Series"]
    data= dict(islice(input_dict.items(), 10))

    return data


def get_time_series_weekly_adjusted_function(user_query:str):

    stock_symbol=query_parser(user_query)
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    data = r.json()
    input_dict=data["Weekly Adjusted Time Series"]
    data= dict(islice(input_dict.items(), 10))

    return data


def get_time_series_monthly_function(user_query:str):

    stock_symbol=query_parser(user_query)
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    data = r.json()
    input_dict=data["Monthly Time Series"]
    data= dict(islice(input_dict.items(), 10))

    return data


def get_time_series_monthly_adjusted_function(user_query:str):

    stock_symbol=query_parser(user_query)
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    data = r.json()
    input_dict=data["Monthly Adjusted Time Series"]
    data= dict(islice(input_dict.items(), 10))

    return data


def get_news_sentiment_function(user_query:str):

    stock_symbol=query_parser(user_query)
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    data = r.json()

    return data


def get_top_gainers_losers_function(user_query:str):

    url = f'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    data = r.json()

    return data


def get_company_overview_function(user_query:str):

    stock_symbol=query_parser(user_query)
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    data = r.json()

    return data
