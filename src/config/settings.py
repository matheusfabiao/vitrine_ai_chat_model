from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='env_files/.env',
        env_file_encoding='utf-8',
    )
    GOOGLE_API_KEY: str
    GOOGLE_AI_MODEL: str
    GOOGLE_AI_TEMPERATURE: float


settings = Settings()
