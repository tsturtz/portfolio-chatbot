from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.config import USER_AGENT

def load_website_docs(urls: list[str]):
    loader = WebBaseLoader(
        urls,
        requests_kwargs={"headers": {"User-Agent": USER_AGENT}}
    )
    return loader.load()

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)

def create_vectorstore(doc_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    vectorstore = Chroma.from_documents(
        documents=doc_chunks,
        embedding=embeddings,
        collection_name="taylorsturtz"
        # persist_directory="./chroma-data"
    )
    return vectorstore
