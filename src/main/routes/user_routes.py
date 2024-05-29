from typing import Dict

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.auth.auth import get_current_user
from src.schemas.user import UserInDB
from src.service.user_service import UserService
from src.models.settings.connection import get_db

router = APIRouter(
  prefix="/user",
  tags=["User"]
)

@router.get("/", status_code=200)
def get_all_user(
  session: Session = Depends(get_db),
  current_user: UserInDB = Depends(get_current_user)
):
    _service = UserService(session)
    return _service.get_all()

@router.get("/{user_id}", status_code=200)
def get_user_by_id(
  user_id: int,
  session: Session = Depends(get_db),
  current_user: UserInDB = Depends(get_current_user)
):
    _service = UserService(session)
    return _service.get_by_id(user_id)

@router.post("/", status_code=201, response_model=Dict)
def register(
  data: Dict,
  session: Session = Depends(get_db)
):
    _service = UserService(session)
    return _service.create(data)

@router.post("/login", status_code=201)
def login(
  data: OAuth2PasswordRequestForm = Depends(),
  session: Session = Depends(get_db)
):
    _service = UserService(session)
    return _service.login(data)

@router.put("/{user_id}", status_code=200, response_model=Dict)
def update_user(
  user_id: int,
  data: Dict,
  session: Session = Depends(get_db)
):
    _service = UserService(session)
    return _service.update(user_id, data)

@router.delete("/{user_id}", status_code=200)
def delete_user(
  user_id: int,
  session: Session = Depends(get_db),
  current_user: UserInDB = Depends(get_current_user)
):
    _service = UserService(session)
    return _service.delete(user_id)


