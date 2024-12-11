import os

from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__name__).absolute().parent
DATA_DIR = BASE_DIR / "data"

load_dotenv(BASE_DIR / ".env")

MODEL_NAME = "gpt-4o-mini"
GOOGLE_API_CREDENTIALS = BASE_DIR / "auth" / "google_api_credentials.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(GOOGLE_API_CREDENTIALS)
PROJECT_ID = os.getenv('PROJECT_ID')
DATASET_NAME = "AI"
TABLE_NAME = "industry_keywords"
LOCATION="asia-northeast1"