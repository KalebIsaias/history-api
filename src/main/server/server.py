from fastapi import APIRouter

from src.main.routes import history_routes
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

router = APIRouter(
  prefix="/api",
)

router.include_router(history_routes.router)