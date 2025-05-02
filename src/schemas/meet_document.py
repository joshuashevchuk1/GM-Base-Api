
from pydantic import BaseModel, Field
from src.database import MeetDocument


class MeetDocumentCreate(BaseModel):
    meet_key: str = Field(..., min_length=1)

def create_meet_document(data: MeetDocumentCreate) -> MeetDocument:
    document = MeetDocument(**data.dict())
    document.save()
    return document
