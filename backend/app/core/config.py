from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str
    PROJECT_NAME: str = "VoxBrief"
     # Configuration for Pydantic settings
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()