# app/core/config.py
import os
from dotenv import load_dotenv
from pydantic import BaseSettings

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL")

    class Config:
        env_file = ".env"

settings = Settings()
