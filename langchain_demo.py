from dotenv import load_dotenv, find_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(find_dotenv())

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

output_parser = StrOutputParser()

query = PromptTemplate.from_template("""

The hotel opens at 8 am and closes at 11 pm.
The menu includes wada pav, chai, and biscuit.
We only have veg options.
There are also rooms available at the hotel.
The wada pav costs Rs. 10, the chai is Rs. 5 and there are multiple types of biscuits available,
ranging from Rs. 10 to Rs. 50

{prompt}
""")

chain = query | model | output_parser

print(chain.invoke({"prompt": "What is the capital of China?"}))


