# app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database
from app.core.config import settings

# Configuração do SQLAlchemy (síncrono)
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Configuração para databases (assíncrono)
database = Database(settings.database_url)
