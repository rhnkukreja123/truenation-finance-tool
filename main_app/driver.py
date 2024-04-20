from qabot_manager_script import QAbotManager
from langchain_openai import ChatOpenAI
import tools.all_tools as all_tools


def initialize_manager():
    turbo_llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    return QAbotManager(tools=[all_tools.finance_domain_tool, all_tools.news_domain_tool], llm=turbo_llm)



query=""

manager=initialize_manager()
response = manager.handle_question(query)


print(f"Answer:{response}")
