from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ClientResponse, ClientUpdate, ClientCreate
from typing import List
from crud import (
    create_client,
    get_clients,
    get_client,
    delete_client,
    update_client,
)

router = APIRouter()


@router.post("/clients/", response_model=ClientResponse)
def create_client_route(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db=db, client=client)


@router.get("/clients/", response_model=List[ClientResponse])
def read_all_clients_route(db: Session = Depends(get_db)):
    clients = get_clients(db)
    return clients


@router.get("/clients/{client_id}", response_model=ClientResponse)
def read_client_route(client_id: int, db: Session = Depends(get_db)):
    db_client = get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="client not found")
    return db_client


@router.delete("/clients/{client_id}", response_model=ClientResponse)
def detele_client_route(client_id: int, db: Session = Depends(get_db)):
    db_client = delete_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="client not found")
    return db_client


@router.put("/clients/{client_id}", response_model=ClientResponse)
def update_client_route(
    client_id: int, client: ClientUpdate, db: Session = Depends(get_db)
):
    db_client = update_client(db, client_id=client_id, client=client)
    if db_client is None:
        raise HTTPException(status_code=404, detail="client not found")
    return db_client