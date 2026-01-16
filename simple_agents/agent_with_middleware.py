from dotenv import load_dotenv, find_dotenv
import os

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.tools import tool

from langchain.agents.middleware import (
    PIIMiddleware,
    SummarizationMiddleware,
    HumanInTheLoopMiddleware
)

load_dotenv(find_dotenv())


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(
    model=llm,
    middleware=[
        PIIMiddleware("email", strategy="redact", apply_to_input=True)
    ],
    system_prompt="You are a helpful assistent."
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "My email is khushal2182002@gmial.com. What is my email ?"}
    ]
})

response = result["messages"][-1].content

print(response)