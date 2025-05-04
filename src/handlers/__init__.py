# handlers/__init__.py
from dns.e164 import to_e164

from .home import router as home
from .health_ import router as health
from .space_name import router as space
from .meet_document import router as meet_document
from .transcript import router as transcript
from .recording import router as recording
from .space_uri import router as space_uri
from .topic_name import router as topic_name
from .convo_history import router as convo_history
from .token import router as token

handlers = [
    home,
    health,
    meet_document,
    space,
    space_uri,
    topic_name,
    transcript,
    recording,
    convo_history,
    token
]
