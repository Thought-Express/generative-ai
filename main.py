from dotenv import load_dotenv, find_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(find_dotenv())

prompt = PromptTemplate.from_template("""
{question}
""")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

output_parser = StrOutputParser()

my_chain = prompt | llm | output_parser

print(my_chain.invoke({"question": "what is the price of a wada pav?"}))