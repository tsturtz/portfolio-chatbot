import chromadb
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.config import EMBEDDING_MODEL, COLLECTION
from src.config import CHROMA_CLOUD_API_KEY, CHROMA_CLOUD_TENANT, CHROMA_CLOUD_DB_ENV


def connect_to_vectorstore():
    """Connects to the Chroma Cloud vectorstore and returns the LangChain wrapper."""

    # Connect to Chroma Cloud using the configuration from setup.py; the collection must already exist from running setup.py
    client = chromadb.CloudClient(
        api_key=CHROMA_CLOUD_API_KEY,
        tenant=CHROMA_CLOUD_TENANT,
        database=CHROMA_CLOUD_DB_ENV
    )
    # Initialize the embedding function for the LangChain wrapper to work
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    # Use the client to create the vectorstore from the existing collection
    vectorstore = Chroma(
        client=client,
        embedding_function=embeddings,
        collection_name=COLLECTION
    )

    return vectorstore
