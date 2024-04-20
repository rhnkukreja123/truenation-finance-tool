from langchain_openai import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.agents import initialize_agent
from langchain.tools import BaseTool, StructuredTool
from langchain.pydantic_v1 import BaseModel, Field
from langchain.agents import Tool
from langchain.tools import BaseTool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper
from functions.finance_functions import (
    get_time_series_daily_function,
    get_quote_endpoint_function,
    get_exchange_rate_function,
    get_time_series_weekly_function,
    get_time_series_weekly_adjusted_function,
    get_time_series_monthly_function,
    get_time_series_monthly_adjusted_function,
    get_news_sentiment_function,
    get_top_gainers_losers_function,
    get_company_overview_function,

)



class Query(BaseModel):
    user_query: str = Field(description="The query to the function")



get_time_series_daily_function_tool = StructuredTool.from_function(
    name='Get_Daily_Time_Series_Function',
    func= get_time_series_daily_function,
    description="To be used for retrieving daily time series data, including open, close, high, and low prices, for a specified stock symbol.",
    args_schema=Query,
    return_direct=False,
)

get_quote_endpoint_function_tool = StructuredTool.from_function(
    name='Get_Quote_Function',
    func= get_quote_endpoint_function,
    description="To be used for querying real-time stock data, including price and volume, for a specific symbol.",
    args_schema=Query,
    return_direct=False,
)

get_exchange_rate_function_tool = StructuredTool.from_function(
    name='Get_Exchange_Rate_Function',
    func= get_exchange_rate_function,
    description="To be used for obtaining the current exchange rate and bid/ask prices between two specified currencies.",
    args_schema=Query,
    return_direct=False,
)


get_time_series_weekly_function_tool=StructuredTool.from_function(
    name='Get_Weekly_Time_Series_Function',
    func= get_time_series_weekly_function,
    description="To retrieve weekly open, high, low, and close prices for a specified stock, summarizing the last trading day of each week.",
    args_schema=Query,
    return_direct=False,
)

get_time_series_weekly_adjusted_function_tool=StructuredTool.from_function(
    name='Get_Weekly_Adjusted_Time_Series_Function',
    func= get_time_series_weekly_adjusted_function,
    description="To retrieve adjusted weekly time series data, including open, high, low, close, adjusted close, volume, and dividends for a specified stock, summarizing the last trading day of each week.",
    args_schema=Query,
    return_direct=False,
)


get_time_series_monthly_function_tool=StructuredTool.from_function(
    name='Get_Monthly_Time_Series_Function',
    func= get_time_series_monthly_function,
    description="To retrieve monthly open, high, low, close, and volume data for a specified stock, summarizing the last trading day of each month.",
    args_schema=Query,
    return_direct=False,
)

get_time_series_monthly_adjusted_function_tool=StructuredTool.from_function(
    name='Get_Monthly_Adjusted_Time_Series_Function',
    func= get_time_series_monthly_adjusted_function,
    description="To retrieve adjusted monthly time series data, including open, high, low, close, adjusted close, volume, and dividends for a specified stock, summarizing the last trading day of each month.",
    args_schema=Query,
    return_direct=False,
)

get_news_sentiment_function_tool=StructuredTool.from_function(
    name='Get_Market_News_and_Sentiment_Data_Function',
    func= get_news_sentiment_function,
    description="To be used to access live and historical market news and sentiment data, covering stocks, cryptocurrencies, forex, and major financial events for comprehensive market analysis",
    args_schema=Query,
    return_direct=False,
)

get_top_gainers_losers_function_tool=StructuredTool.from_function(
    name='Get_Market_Movers_Function',
    func= get_top_gainers_losers_function,
    description="To be used to retrieve the top 20 gainers, losers, and most actively traded tickers in the US market.",
    args_schema=Query,
    return_direct=False,
)

get_company_overview_function_tool=StructuredTool.from_function(
    name='Get_Company_Financials_Function',
    func= get_company_overview_function,
    description="To be used to access company information, financial ratios, and key metrics, updated as soon as new earnings and financial reports are released.",
    args_schema=Query,
    return_direct=False,
)


def get_all_finance_tools():
    tools=[
        get_time_series_daily_function_tool,
        get_quote_endpoint_function_tool, 
        get_exchange_rate_function_tool, 
        get_time_series_weekly_function_tool,
        get_time_series_weekly_adjusted_function_tool,
        get_time_series_monthly_function_tool,
        get_time_series_monthly_adjusted_function_tool,
        get_news_sentiment_function_tool,
        get_top_gainers_losers_function_tool,
        get_company_overview_function_tool
        ]

    return tools
