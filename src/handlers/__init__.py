# handlers/__init__.py

from .home import router as home
from .health_ import router as health
from .space_name import router as space
from .meet_document import router as meet_document

handlers = [home, health, space, meet_document]
