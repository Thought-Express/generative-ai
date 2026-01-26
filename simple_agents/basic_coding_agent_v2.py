from langchain.agents import create_agent

import os
from dotenv import load_dotenv, find_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool

load_dotenv(find_dotenv())

@tool
def create_python_file(filename: str, content: str) -> str:
    """
    Creates a python file, with the given filename and content

    We omit the .py extension from the filename
    if the file is created successfully, return True, else False

    """

    try:
        with open(filename + '.py', 'w') as f:
            f.write(content)
        return "True"
    except Exception as e:
        return "False"

@tool
def read_file(filename: str) -> str:
    """
    Reads a file and returns the content
    give the full file path with the extension
    """

    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        return "Error reading file"

# 2. Setup LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

my_agent = create_agent(
    model=llm,
    tools=[create_python_file, read_file]
)

query = """
Make a python program for me, called "print_pi_digits.py", 
and the requirements for what the program should do, is in the file 
"what_I_need.md"
"""

response = my_agent.invoke({"messages": ("human", query)})
result = response["messages"][-1].content

print(result)