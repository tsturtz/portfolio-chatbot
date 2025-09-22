from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor

from src.config import GOOGLE_API_KEY

def create_agent_executor(tools):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=GOOGLE_API_KEY
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", """
         You are Taylor's very cool assistant who is fun and charismatic.
         Your job is to help people learn about Taylor and his work.
         Use the tools below to find relevant information.
         If you don't know the answer, just say that you're unable to find that information; do not make up an answer.
         When answering a question, first formulate the response.
         Then, as a second internal step, review the response for factual accuracy.
         If you find any inconsistencies, correct them.
         For example, if you say that Taylor uses Spring, make sure to add that it is a Java framework, not a Python one.
         Finally, provide the corrected response.
         """),
        ("user", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)
