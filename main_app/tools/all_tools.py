from langchain_openai import ChatOpenAI
from langchain.agents import Tool
from langchain.tools import BaseTool

from tools import finance_tool
from functions import news_function
from tools.finance_agent import FinanceDomainManager



tools=finance_tool.get_all_finance_tools()
llm =ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')



finance_domain_tool = Tool(
    name='Finance Domain Tool',
    func= FinanceDomainManager(tools=tools).agent_executor_multihop,
    description="This function should be used whenever we need to answer any finance based question like sentiments or price"
)

news_domain_tool = Tool(
    name='News Domain Tool',
    func= news_function.news_domain_tool_function,
    description="This function should be used whenever we need to answer any news based question"
)
