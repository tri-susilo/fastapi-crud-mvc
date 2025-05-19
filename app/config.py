import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Settings:
    APP_NAME: str = "FASTAPI MVC API"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    print("⚠️ DEBUG (with path):", DATABASE_URL)

settings = Settings()