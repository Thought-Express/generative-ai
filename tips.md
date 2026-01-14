## To build a enviornment from scratch

### Install python 3.11

### Create a virtual enviornment
python -m venv .venv

### Run the install command
python -m pip install --no-cache-dir -U langchain /
    langchain-community langchain-core langchain-google-genai /
    faiss-cpu python-dotenv langchain-huggingface sentence-transformers

