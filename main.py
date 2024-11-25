from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv
import os
from pydantic import BaseModel

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o motor de conexão
engine = create_engine(DATABASE_URL)

# Cria uma sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a base para os modelos
Base = declarative_base()

# Define um modelo de exemplo
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255), index=True)

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicializa o FastAPI
app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define os schemas usando Pydantic para validação
class ItemCreate(BaseModel):
    name: str
    description: str

class ItemRead(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True

# Rota para criar um novo item
@app.post("/items/", response_model=ItemRead)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Rota para listar todos os itens
@app.get("/items/", response_model=list[ItemRead])
def read_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items
