"""Configuration for the backend."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    # MongoDB settings
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_database: str = "nerxiv"

    # Ollama settings
    ollama_host: str = "http://localhost:11434"

    # API settings
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()
