from fastapi import APIRouter, Depends, HTTPException
from src.models.users.schemas import UserResponseDTO, UserAccessor, UserCreateDTO, UserSerializer
from src.database.session import get_db
from sqlalchemy.orm import Session
from typing import Any
router = APIRouter()

@router.get("/{id}", response_model=UserResponseDTO)
def get_user(
    *,
    db: Session = Depends(get_db),
    id: str,
)->Any:
    """
    Get A Dummy User from DB
    :param db:
    :param id:
    :return:
    """
    user_ = UserAccessor.get_by_id(
        resource_id=id, db_session=db
    )
    if not user_:
        raise HTTPException(status_code=404, detail="Item not found")
    return user_

@router.post("/", response_model=UserResponseDTO)
def create_user(
    *,
    db: Session = Depends(get_db),
    dummy_user_in: UserCreateDTO,
) -> Any:
    """
    Create a Dummy User on System
    :param db:
    :param dummy_user_in:
    :return:
    """
    dummy_user = UserSerializer.create(
        name=dummy_user_in.name,
        surname=dummy_user_in.surname
    )
    UserAccessor.add(
        entity=dummy_user, db_session=db
    )
    return dummy_user