from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vector_store = FAISS.load_local("hotel_vector_store", embeddings, allow_dangerous_deserialization=True)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

retriever = vector_store.as_retriever()

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
)

result = qa_chain.invoke({"query": "Do you have non-veg food?"})

print(result["result"])

print("Source documents:")
for doc in result["source_documents"]:
    print(doc.page_content)
    print("Metadata:", doc.metadata)
    print("-" * 80)