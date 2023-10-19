from fastapi import APIRouter, Body, Depends, HTTPException
from typing import Any
dummy_router = APIRouter()
from sqlalchemy.orm import Session
from app.schemas.health_check import  HealthCheckResponse
from app.schemas.dummy_user import  DummyUser, DummyUserCreate
from app.db.session import  get_db
from app import crud



@dummy_router.get("/health_check", response_model=HealthCheckResponse)
def health_check_dummy()-> Any:
    return {"msg": "Health Check from dummy router"}

@dummy_router.get("/{id}", response_model=DummyUser)
def get_dummy_users(
    *,
    db: Session = Depends(get_db),
    id: int,
)->Any:
    """
    Get A Dummy User from DB
    :param db:
    :param id:
    :return:
    """
    dummy_user = crud.dummy_user.get(db=db, id=id)
    if not dummy_user:
        raise HTTPException(status_code=404, detail="Item not found")
    return dummy_user

@dummy_router.post("/", response_model=DummyUser)
def create_item(
    *,
    db: Session = Depends(get_db),
    dummy_user_in: DummyUserCreate,
) -> Any:
    """
    Create a Dummy User on System
    :param db:
    :param dummy_user_in:
    :return:
    """
    dummy_user = crud.dummy_user.create(db, obj_in = dummy_user_in)
    return dummy_user
