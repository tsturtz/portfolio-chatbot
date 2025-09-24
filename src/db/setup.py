import chromadb

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_community import GoogleDriveLoader
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

# Load documents from Google Drive
google_docs_loader = GoogleDriveLoader(
    file_ids=["1melJsJNEMtqik7--dOQy0OO15OH12BzoPZqgwlV33z4"],
)
google_docs = google_docs_loader.load()
print(f"Loaded {len(google_docs)} documents from Google Drive.")

# Scrape website content
web_loader = WebBaseLoader(
    [
        "https://taylorsturtz.com",
        "https://taylorsturtz.com/resume",
        "https://github.com/tsturtz",
        "https://www.mobygames.com/person/1309509/taylor-sturtz/"
    ],
    requests_kwargs={"headers": {"User-Agent": USER_AGENT}}
)
web_docs = web_loader.load()
print(f"Loaded {len(web_docs)} documents from websites.")

# Combine documents from both loaders into a single list
all_docs = web_docs + google_docs

# Split documents into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
split_docs = splitter.split_documents(all_docs)
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
