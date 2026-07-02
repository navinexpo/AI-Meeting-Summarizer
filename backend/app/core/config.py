import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# प्रोजेक्ट की रूट (backend) डायरेक्टरी का पाथ
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    GROQ_API_KEY: str
    PROJECT_NAME: str = "VoxBrief"

    # Pydantic v2 के लिए सही कॉन्फ़िगरेशन सिंटैक्स
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()