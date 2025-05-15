from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='env_files/.env',
        env_file_encoding='utf-8',
    )
    OLLAMA_AI_MODEL: str
    OLLAMA_AI_TEMPERATURE: float


settings = Settings()
