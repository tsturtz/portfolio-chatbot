from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor

from src.config import LANGUAGE_MODEL, GOOGLE_API_KEY


def create_agent_executor(tools):
    """Creates agent from model and provides tools."""

    llm = ChatGoogleGenerativeAI(
        model=LANGUAGE_MODEL,
        google_api_key=GOOGLE_API_KEY
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", """
         You are Taylor's helpful and professional assistant who is fun and charismatic.
         Your sole purpose is to provide factual information about Taylor and his work based only on the documents provided.
         Never provide information that is not in your documents. If a question cannot be answered from the provided documents, state that you are unable to find that information.
         Do not make up any answers.
         """),
        ("user", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

    return AgentExecutor(agent=agent, tools=tools, verbose=True)
