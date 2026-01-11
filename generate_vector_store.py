from langchain_core.documents import Document
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("./hotel-info.txt", "r") as file:
    hotel_info = file.read()

splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = splitter.split_text(hotel_info)

docs = [Document(page_content=chunk) for chunk in chunks]

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

vector_store = FAISS.from_documents(docs, embeddings)

vector_store.save_local("hotel_vector_store")


