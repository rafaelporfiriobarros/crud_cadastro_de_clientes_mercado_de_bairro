from pydantic import BaseModel, PositiveFloat, EmailStr, field_validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional


class ClientBase(BaseModel):
    nome: str
    telefone: str
    endereco: str
    cpf: str
    email: EmailStr
    data_nascimento: datetime
    data_ultimo_pedido: datetime
    saldo_devedor: float
    observacoes: str

class ClientCreate(ClientBase):
    pass

class ClientResponse(ClientBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ClientUpdate(BaseModel):
    nome: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    data_nascimento: Optional[datetime] = None
    data_ultimo_pedido: Optional[datetime] = None
    saldo_devedor: Optional[float] = None
    observacoes: Optional[str] = None

