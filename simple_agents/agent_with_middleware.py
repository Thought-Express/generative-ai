from dotenv import load_dotenv, find_dotenv
import os

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.agents.middleware import PIIMiddleware

load_dotenv(find_dotenv())


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(
    model=llm,
    system_prompt="You are a helpful assistent.",
    middleware=[
        PIIMiddleware("phone_number", detector=(
            r"(?:\+?\d{1,3}[\s.-]?)?"
            r"(?:\(?\d{2,4}\)?[\s.-]?)?"
            r"\d{3,4}[\s.-]?\d{4}"
        ), apply_to_input=True, strategy="redact")
    ]
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "My email is +91 55555 55555. What is my email ?"}
    ]
})

response = result["messages"][-1].content

print(response)