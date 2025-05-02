from pydantic import BaseModel
from io import BytesIO
from typing import Optional

class MeetDocumentUploadTranscript(BaseModel):
    transcript: Optional[BytesIO] = None  # This will handle the generic file
