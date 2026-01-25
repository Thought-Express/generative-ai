from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt

import os
from dotenv import load_dotenv, find_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv(find_dotenv())

# 1. Setup Embeddings and Vector Store
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.load_local("hotel_vector_store_local", embeddings, allow_dangerous_deserialization=True)
retriever = vector_store.as_retriever()

# 2. Setup LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

@dynamic_prompt
def prompt_with_context(request):
    message = request.messages[-1].content
    retrived_docs = retriever.invoke(message)

    context = "\n\n".join([doc.page_content for doc in retrived_docs])

    system_prompt = (
        "You are a chat assistent for a 5 star hotel, who talks in a very humarous way"
        "Answer the questions based on the context given"
        "If you don't know the answer just say so, don't make up answers"

        f"context: {context}"
    )

    return system_prompt


my_agent = create_agent(
    model=llm,
    middleware = [
        prompt_with_context
    ]
)

query = "Do you have biscuits ?"

response = my_agent.invoke({"messages": ("human", query)})
result = response["messages"][-1].content

print(result)