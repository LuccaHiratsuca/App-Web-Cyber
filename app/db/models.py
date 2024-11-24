# app/db/models.py
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idade = Column(Integer)