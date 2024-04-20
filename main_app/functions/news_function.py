from langchain.utilities import GoogleSerperAPIWrapper
import os


def news_domain_tool_function(search_query):
    search = GoogleSerperAPIWrapper(type="news", tbs="qdr:w1", serper_api_key="add0c7de24460962d14a5c84726d0eae6f97a684")
    result_dict = search.results(search_query)
    answer=result_dict["news"][0]['snippet']
    return answer

