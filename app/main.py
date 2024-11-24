# app/main.py
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.db.database import database, engine
from app.db import models
from app.routers import users

# Cria as tabelas no banco de dados (se ainda não existirem)
models.Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conecta ao banco de dados na inicialização
    await database.connect()
    yield
    # Desconecta do banco de dados no encerramento
    await database.disconnect()

app = FastAPI(
    title="Meu Serviço FastAPI",
    description="API para gerenciamento de usuários",
    version="1.0.0",
    lifespan=lifespan
)

# Configuração de CORS (opcional, ajuste conforme necessário)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Altere para os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui os routers
app.include_router(users.router)
