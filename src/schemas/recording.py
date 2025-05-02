from pydantic import BaseModel
from io import BytesIO
from typing import Optional

class MeetDocumentUploadRecording(BaseModel):
    recording: Optional[BytesIO] = None
