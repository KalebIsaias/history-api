from fastapi import APIRouter

from src.main.routes import history_routes
from src.main.routes import user_routes

router = APIRouter(
  prefix="/api",
)

router.include_router(history_routes.router)
router.include_router(user_routes.router)