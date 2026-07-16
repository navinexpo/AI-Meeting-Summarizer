import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
# Define the base directory of the project by resolving the path of the current file and navigating up three levels in the directory structure. This is useful for locating configuration files and other resources relative to the project's root directory.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    GROQ_API_KEY: str
    PROJECT_NAME: str = "VoxBrief"
#
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )
# Set the settings instance
settings = Settings()