from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Employee Knowledge Assistant"
    environment: str = "development"

    database_url: str

    neo4j_uri: str
    neo4j_username: str
    neo4j_password: str

    openai_api_key: str

    api_key: str

    cors_origins: str = "http://localhost:8501"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()
