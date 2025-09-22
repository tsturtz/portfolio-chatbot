import os
from dotenv import load_dotenv

load_dotenv()

COLLECTION = "taylorsturtz"
EMBEDDING_MODEL = "models/gemini-embedding-001"
LANGUAGE_MODEL = "gemini-2.5-flash-lite"

USER_AGENT = os.getenv("USER_AGENT", "Mozilla/5.0")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

CHROMA_CLOUD_API_KEY = os.getenv("CHROMA_CLOUD_API_KEY")
CHROMA_CLOUD_TENANT = os.getenv("CHROMA_CLOUD_TENANT")
CHROMA_CLOUD_DB_ENV = os.getenv("CHROMA_CLOUD_DB_ENV")
