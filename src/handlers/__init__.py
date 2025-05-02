# handlers/__init__.py

from .home import router as home_router
from .health_ import router as health_router
from src.schemas.transcript import router as transcript_router

routers = [home_router, health_router,transcript_router]
