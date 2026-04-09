# memory/vector_store.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def build_vector_store(docs):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(docs, embeddings)
