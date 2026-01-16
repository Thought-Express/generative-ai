from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt

from dotenv import load_dotenv, find_dotenv
import os

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(find_dotenv())

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.load_local("../hotel_vector_store_local", embeddings, allow_dangerous_deserialization=True)
retriever = vector_store.as_retriever()

@dynamic_prompt
def prompt_with_context(request):
    query = request.state["messages"][-1].content
    retrieved_docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    system_prompt = (
        "Use the given context to answer the question. "
        "If you don't know the answer, say you don't know. "
        f"Context: {context}"
    )
    return system_prompt

query = "Do you have non veg options ?"

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(
    model=llm,
    middleware=[
        prompt_with_context
    ],
)


response = agent.invoke({"messages": ("human", query)})
answer = response["messages"][-1].content

print(answer)