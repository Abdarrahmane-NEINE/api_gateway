from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SERVICE1_URL: str = "http://localhost:9001"
    SERVICE2_URL: str = "http://localhost:9002"
    SECRET_KEY: str = "secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    RATE_LIMIT: int = 100  # requests per minute
    IDP_PUBLIC_KEY: str = "key"

    # Open-Closed Principle by allowing extension via environment variables.
    class Config:
        env_file = ".env"


settings = Settings()  # Global settings instance (read-only)
