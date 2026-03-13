import os
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def search(query:str) ->str:
    """
    "Returns the current weather for a given location.
    """
    print(f"Searching  for {query}")
    return "Tokyo weather is sunny"

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
tools=[search]
agent=create_agent(model=llm,tools=tools)


def main():
    print("Hello from langchain-course!")
    result=agent.invoke({"messages":[HumanMessage(content="what is the weather in Tokyo")]})
    print(result)


if __name__ == "__main__":
    main()
