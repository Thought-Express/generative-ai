from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from langchain_google_genai import ChatGoogleGenerativeAI

gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

from langchain.tools import tool

# Setup LLM
llm = ChatOllama(model="qwen2.5-coder:7b")

@tool
def write_to_a_file(file_name: str, content: str) -> str:
    """
    This function can be used to write to a file, it takes in a
    file name and creates that file, and overwrites if it already exists
    and writes the content to it.

    And if the file is created, it returns File Created ! else error !!
    """

    try:
        with open(file_name, "w") as f:
            f.write(content)
            return "File Created"
    except Exception as e:
        return str(e)



my_agent = create_agent(
    model=gemini,
    tools=[write_to_a_file]
)

query = "Make a python file called reverse.py in the current directory, that can reverse a python linked list"

response = my_agent.invoke({"messages": ("human", query)})
result = response["messages"][-1].content

print(result)