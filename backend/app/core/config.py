import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    GROQ_API_KEY: str
    PROJECT_NAME: str = "VoxBrief"
# Set the configuration for the Settings class, specifying the location of the environment file and its encoding. The 'extra' parameter is set to "ignore" to allow for additional environment variables that are not explicitly defined in the Settings class.
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()