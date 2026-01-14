from dotenv import load_dotenv, find_dotenv
import os

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.tools import tool

load_dotenv(find_dotenv())

@tool
def create_python_file(filename: str, content: str) -> str:
    """Create a python file. Returns true of the file was created, else false

    Args:
        filename: The name of the file to create. 
            The file gets created in the same directory
            The filename should not include the .py extension
        content: The content to write in the file
    """

    try:
        with open(filename + '.py', 'w') as f:
            f.write(content)
        return "True"
    except Exception as e:
        return "False"


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(
    model=llm,
    tools=[create_python_file],
    system_prompt="You are a helpful python coding assistant."
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "Create a python script called fibo.py that prints the Fibonacci sceries till the 10th numebr"}
    ]
})

print(result)