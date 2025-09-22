import os
from dotenv import load_dotenv

load_dotenv()

USER_AGENT = os.getenv("USER_AGENT", "Mozilla/5.0")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
