from dotenv import load_dotenv, find_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(find_dotenv())

# 1. Setup Embeddings and Vector Store
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.load_local("hotel_vector_store_local", embeddings, allow_dangerous_deserialization=True)
retriever = vector_store.as_retriever()

# 2. Setup LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 3. Create the System Prompt (Required in 1.x)
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer, just say that you don't know. "
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# 4. Build the RAG Chain
# create_stuff_documents_chain handles the formatting of context into the prompt
question_answer_chain = create_stuff_documents_chain(llm, prompt)
# create_retrieval_chain connects the retriever to the QA chain
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# 5. Run the query
response = rag_chain.invoke({"input": "Do you have non-veg food?"})

# 6. Output Results
print(response["answer"])

print("\nSource documents:")
for doc in response["context"]:
    print(doc.page_content)
    print("Metadata:", doc.metadata)
    print("-" * 80)