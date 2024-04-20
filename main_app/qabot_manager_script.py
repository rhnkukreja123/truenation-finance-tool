import tools.all_tools as all_tools
from langchain_openai import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.agents import initialize_agent


class QAbotManager:
    def __init__(self, tools, llm):
        self.tools = tools
        self.llm = llm
        
        self.memory = ConversationBufferWindowMemory(
            memory_key='chat_history',
            k=3,
            return_messages=True
        )

        self.conversational_agent = initialize_agent(
        agent='chat-conversational-react-description',
        tools=self.tools,
        llm=self.llm,
        verbose=True,
        max_iterations=3,
        early_stopping_method='generate',
        memory=self.memory
        )

    def handle_question(self, question):

        conversational_agent = self.conversational_agent
        response_dict = conversational_agent(question)
        response = response_dict["output"]
            

        return response
