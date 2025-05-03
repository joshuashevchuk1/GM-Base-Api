from pydantic import BaseModel
from io import BytesIO
from typing import Optional

class MeetDocumentToken(BaseModel):
    token: Optional[BytesIO] = None
