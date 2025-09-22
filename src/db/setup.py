import chromadb

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from ..config import EMBEDDING_MODEL, COLLECTION
from ..config import CHROMA_CLOUD_API_KEY, CHROMA_CLOUD_TENANT, CHROMA_CLOUD_DB_ENV
from ..config import USER_AGENT


# Connect to Chroma Cloud
client = chromadb.CloudClient(
  api_key=CHROMA_CLOUD_API_KEY,
  tenant=CHROMA_CLOUD_TENANT,
  database=CHROMA_CLOUD_DB_ENV
)

# Delete existing collection if it exists
try:
    client.delete_collection(COLLECTION)
    print("Existing collection deleted.")
except Exception:
    print("Collection does not exist, proceeding to create a new one.")

# Scrape website content
loader = WebBaseLoader(
    [
        "https://taylorsturtz.com",
        "https://taylorsturtz.com/resume",
        "https://github.com/tsturtz",
        "https://www.mobygames.com/person/1309509/taylor-sturtz/"
    ],
    requests_kwargs={"headers": {"User-Agent": USER_AGENT}}
)
docs = loader.load()
print(f"Loaded {len(docs)} documents from website.")

# Split documents into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
split_docs = splitter.split_documents(docs)
print(f"Split into {len(split_docs)} chunks.")

# Create embeddings and vector store in cloud client, via the LangChain wrapper
embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
vectorstore = Chroma(
    client=client,
    embedding_function=embeddings,
    collection_name=COLLECTION
)
vectorstore.add_documents(documents=split_docs)
print("Chroma vectorstore created and populated.")