# app/schemas/user.py
from pydantic import BaseModel, Field

class UsuarioBase(BaseModel):
    nome: str = Field(..., example="Maria")
    idade: int = Field(..., ge=0, example=30)

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    pass

class UsuarioRead(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
