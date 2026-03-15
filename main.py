import os
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch, tavily_search


llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
tools=[TavilySearch()]
agent=create_agent(model=llm,tools=tools)


def main():
    print("Hello from langchain-course!")
    result=agent.invoke({"messages":[HumanMessage(content="Search for top 10 MES job opening in canada which are in S&P 500 or similer comapny. search only active jobs that are accepting application")]})
    print(result)


if __name__ == "__main__":
    main()
