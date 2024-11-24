# app/db/crud.py
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db import models, schemas

def get_usuario(db: Session, usuario_id: int) -> Optional[models.Usuario]:
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 10) -> List[models.Usuario]:
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate) -> models.Usuario:
    db_usuario = models.Usuario(nome=usuario.nome, idade=usuario.idade)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: schemas.UsuarioUpdate) -> Optional[models.Usuario]:
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario:
        db_usuario.nome = usuario.nome
        db_usuario.idade = usuario.idade
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int) -> Optional[models.Usuario]:
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario
