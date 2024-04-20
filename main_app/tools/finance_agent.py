from langchain_openai import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.agents import initialize_agent
from langchain.tools import BaseTool, StructuredTool
from langchain.pydantic_v1 import BaseModel, Field
from langchain.agents import Tool
from langchain.tools import BaseTool
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent, create_openai_tools_agent
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper

from tools import finance_tool
import prompts



class FinanceDomainManager:
    def __init__(self, tools):
        self.tools = tools
        self.prompt_oai_tools = hub.pull("hwchase17/openai-tools-agent")

    def agent_executor_multihop(self, question):
        prompt_oai_tools=self.prompt_oai_tools
        prompt_oai_tools.messages[0].prompt.template=prompts.finance_agent_prompt

        oaitools_agent = create_openai_tools_agent(ChatOpenAI(), self.tools, prompt_oai_tools)
        oaitools_agent_executor = AgentExecutor(
            agent=oaitools_agent, tools=self.tools, verbose=True, handle_parsing_errors=True
        )

        answer=oaitools_agent_executor.invoke({"input": question})

        return answer


