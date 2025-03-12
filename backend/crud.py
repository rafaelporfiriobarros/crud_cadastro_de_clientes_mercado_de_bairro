from sqlalchemy.orm import Session
from schemas import ClientUpdate, ClientCreate
from models import ClientModel

def get_client(db: Session, client_id: int):
    """
    funcao que recebe um id e retorna somente ele
    """
    return db.query(ClientModel).filter(ClientModel.id == client_id).first()

def get_clients(db: Session):
    """
    funcao que retorna todos os elementos
    """
    return db.query(ClientModel).all()

def create_client(db: Session, client: ClientCreate):
    db_client = ClientModel(**client.model_dump())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def delete_client(db: Session, client_id: int):
    db_client = db.query(ClientModel).filter(ClientModel.id == client_id).first()
    db.delete(db_client)
    db.commit()
    return db_client

def update_client(db: Session, client_id: int, client: ClientUpdate):
    db_client = db.query(ClientModel).filter(ClientModel.id == client_id).first()

    if db_client is None:
        return None
    
    if client.nome is not None:
        db_client.nome = client.nome
    if client.telefone is not None:
        db_client.telefone = client.telefone
    if client.endereco is not None:
        db_client.endereco = client.endereco
    if client.cpf is not None:
        db_client.cpf = client.cpf
    if client.email is not None:
        db_client.email = client.email
    if client.data_nascimento is not None:
        db_client.data_nascimento = client.data_nascimento
    if client.data_ultimo_pedido is not None:
        db_client.data_ultimo_pedido = client.data_ultimo_pedido
    if client.saldo_devedor is not None:
        db_client.saldo_devedor = client.saldo_devedor
    if client.observacoes is not None:
        db_client.observacoes = client.observacoes

    db.commit()
    return db_client