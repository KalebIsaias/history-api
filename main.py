from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.config.settings import settings
from src.main.server.server import router
from src.utils.init_db import create_tables

app = FastAPI(
    debug=bool(settings.DEBUG),
    title=settings.TITLE,
)

@app.on_event("startup")
def on_startup() -> None:
    create_tables()

if settings.DEBUG:
    origins = ["*"]
else:
    origins = [
        str(origin).strip(",") for origin in settings.ORIGINS
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)