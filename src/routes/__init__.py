# routes/__init__.py

from .home_route import router as home_router
from .health_route import router as health_router
from .transcript import router as transcript_router

routers = [home_router, health_router,transcript_router]
