from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.auth.auth import get_current_user
from src.models.settings.connection import get_db
from src.schemas.user import UserInDB
from src.service.history_service import HistoryService


router = APIRouter(
  prefix="/history",
  tags=["History"]
)

@router.get("/", status_code=200)
def get_all_history(
  session: Session = Depends(get_db),
  current_user: UserInDB = Depends(get_current_user)
):
    _service = HistoryService(session)
    return _service.get_all()

@router.get("/{history_id}", status_code=200)
def get_history_by_id(
  history_id: int,
  session: Session = Depends(get_db),
  current_user: UserInDB = Depends(get_current_user)
):
    _service = HistoryService(session)
    return _service.get_by_id(history_id)

@router.post("/", status_code=201, response_model=Dict)
def create_history(
  data: Dict,
  session: Session = Depends(get_db),
  current_user: UserInDB = Depends(get_current_user)
):
    _service = HistoryService(session)
    return _service.create(data)

@router.post("/{history_id}/enhance", status_code=200)
def enhance_history(
  history_id: int,
  session: Session = Depends(get_db),
  current_user: UserInDB = Depends(get_current_user)
):
    _service = HistoryService(session)
    return _service.enchance_history(history_id)

@router.put("/{history_id}", status_code=200, response_model=Dict)
def update_history(
  history_id: int,
  data: Dict,
  session: Session = Depends(get_db),
  current_user: UserInDB = Depends(get_current_user)
):
    _service = HistoryService(session)
    return _service.update(history_id, data)

@router.delete("/{history_id}", status_code=200)
def delete_history(
  history_id: int,
  session: Session = Depends(get_db),
  current_user: UserInDB = Depends(get_current_user)
):
    _service = HistoryService(session)
    return _service.delete(history_id)