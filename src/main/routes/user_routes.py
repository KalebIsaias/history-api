from typing import Dict

from fastapi import APIRouter, Depends, HTTPException

from src.service.user_service import UserService

router = APIRouter(
  prefix="/user",
  tags=["User"]
)

@router.get("/", status_code=200)
def get_all_user():
    _service = UserService()
    return _service.get_all()

@router.get("/{user_id}", status_code=200)
def get_user_by_id(
  user_id: int
):
    _service = UserService()
    return _service.get_by_id(user_id)

@router.post("/", status_code=201, response_model=Dict)
def create_user(
  data: Dict
):
    _service = UserService()
    return _service.create(data)

@router.put("/{user_id}", status_code=200, response_model=Dict)
def update_user(
  user_id: int,
  data: Dict
):
    _service = UserService()
    return _service.update(user_id, data)

@router.delete("/{user_id}", status_code=200)
def delete_user(
  user_id: int
):
    _service = UserService()
    return _service.delete(user_id)