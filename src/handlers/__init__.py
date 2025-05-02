# handlers/__init__.py

from .home import router as home
from .health_ import router as health

handlers = [home, health]
