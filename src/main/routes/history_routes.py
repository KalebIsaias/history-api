from typing import Dict

from fastapi import APIRouter, Depends, HTTPException

from src.service.history_service import HistoryService

router = APIRouter(
  prefix="/history",
)

@router.get("/hello", status_code=200)
def hello_world():
    return {"message": "Hello World"}


@router.post("/", status_code=201, response_model=Dict)
def create_history(
    data: Dict
):
    _service = HistoryService()
    return _service.create(data)