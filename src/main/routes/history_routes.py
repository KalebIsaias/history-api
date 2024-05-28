from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.service.history_service import HistoryService
from src.models.settings.connection import get_db

router = APIRouter(
  prefix="/history",
  tags=["History"]
)

@router.get("/", status_code=200)
def get_all_history(
  session: Session = Depends(get_db)
):
    _service = HistoryService(session)
    return _service.get_all()

@router.get("/{history_id}", status_code=200)
def get_history_by_id(
  history_id: int,
  session: Session = Depends(get_db)
):
    _service = HistoryService(session)
    return _service.get_by_id(history_id)

@router.post("/", status_code=201, response_model=Dict)
def create_history(
  data: Dict,
  session: Session = Depends(get_db)
):
    _service = HistoryService(session)
    return _service.create(data)

@router.put("/{history_id}", status_code=200, response_model=Dict)
def update_history(
  history_id: int,
  data: Dict,
  session: Session = Depends(get_db)
):
    _service = HistoryService(session)
    return _service.update(history_id, data)

@router.delete("/{history_id}", status_code=200)
def delete_history(
  history_id: int,
  session: Session = Depends(get_db)
):
    _service = HistoryService(session)
    return _service.delete(history_id)