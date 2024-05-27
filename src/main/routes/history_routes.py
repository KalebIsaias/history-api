from typing import Dict

from fastapi import APIRouter, Depends, HTTPException

from src.service.history_service import HistoryService

router = APIRouter(
  prefix="/history",
  tags=["History"]
)

@router.get("/", status_code=200)
def get_all_history():
    _service = HistoryService()
    return _service.get_all()

@router.get("/{history_id}", status_code=200)
def get_history_by_id(
  history_id: int
):
    _service = HistoryService()
    return _service.get_by_id(history_id)

@router.post("/", status_code=201, response_model=Dict)
def create_history(
  data: Dict
):
    _service = HistoryService()
    return _service.create(data)

@router.put("/{history_id}", status_code=200, response_model=Dict)
def update_history(
  history_id: int,
  data: Dict
):
    _service = HistoryService()
    return _service.update(history_id, data)

@router.delete("/{history_id}", status_code=200)
def delete_history(
  history_id: int
):
    _service = HistoryService()
    return _service.delete(history_id)