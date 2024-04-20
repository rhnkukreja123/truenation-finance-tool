finance_agent_prompt="""Answer the following questions as best you can. You have access to the following tools:

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, make sure to first convert the currency into USD then only calculate the percentage difference between the amounts
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

"""


