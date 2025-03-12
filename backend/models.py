from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from sqlalchemy.sql import func
from database import Base


class ClientModel(Base):
    __tablename__ = "clients"  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False, index=True)
    telefone = Column(String(20), index=True)
    endereco = Column(String, index=True)
    cpf = Column(String(11), unique=True, index=True)
    email = Column(String(100), index=True)
    data_nascimento = Column(Date, index=True)
    data_ultimo_pedido = Column(Date, index=True)
    saldo_devedor = Column(Float, default=0.0, index=True)
    observacoes = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)