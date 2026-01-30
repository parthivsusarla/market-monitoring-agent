import time
from groq import APIConnectionError

from langchain_groq import ChatGroq
from langchain.agents.agent import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain.prompts import PromptTemplate

from agent.tools import search_market_news
from agent.prompts import SYSTEM_PROMPT
from config import GROQ_API_KEY, MODEL_NAME


def run_agent(topic: str) -> str:
    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=MODEL_NAME,
        temperature=0.2,
    )

    tools = [search_market_news]

    prompt = PromptTemplate.from_template(
    SYSTEM_PROMPT
    + """

You have access to the following tools:
{tools}

Tool names:
{tool_names}

Rules:
- You may use the news tool at most ONCE
- After receiving news, you MUST produce a classification
- Do not loop or repeat actions

Use the following format:

Question: the input question
Thought: decide whether news lookup is needed
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
Thought: I now know the classification
Final Answer:
Classification: IMPORTANT or IGNORE
Reason:
- explanation
Impact Summary:
- market impact

Question: {input}
{agent_scratchpad}
"""
)

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )

    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
    )

    result = executor.invoke({"input": topic})

    # Safety: never return None to UI
    output = result.get("output")
    if not output:
        return "No significant market-impacting developments were found for the given topic."

    return output
