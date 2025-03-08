import os
from urllib.parse import quote_plus


class Settings:
    # Project
    PROJECT_NAME: str = "Products Management API"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_DESCRIPTION: str = "A simple API to manage products"

    # Database settings
    MONGODB_HOST: str = os.environ.get("MONGODB_HOST", "mongodb")
    MONGODB_PORT: int = int(os.environ.get("MONGODB_PORT", 27017))
    MONGODB_USER: str = quote_plus(os.environ.get("MONGODB_USER",""))
    MONGODB_PASSWORD: str = quote_plus(os.environ.get("MONGODB_PASS", ""))


settings = Settings()
