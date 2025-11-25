import os

# Semantic Scholar API
S2_API_BASE = os.getenv("S2_API_BASE", "https://api.semanticscholar.org/graph/v1")
S2_API_KEY = os.getenv("S2_API_KEY", "")  # <-- 正確！讀環境變數 S2_API_KEY

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./arrn.db")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'aarn.db')}"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

APP_NAME = "Approximation Algorithm Research Navigator"

DB_URL = "sqlite:///./arrn.db"
