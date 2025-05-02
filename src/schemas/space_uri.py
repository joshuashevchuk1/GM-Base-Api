from src.database.model import MeetDocument
from pydantic import BaseModel, Field

class MeetDocumentSpaceUriUpdate(BaseModel):
    space_uri: str = Field(..., min_length=1)

def get_space_uri(meet_key: str) -> str:
    document = MeetDocument.objects.get(meet_key=meet_key)
    return document.space_uri

def put_topic_name(meet_key: str, update_data: MeetDocumentSpaceUriUpdate) -> MeetDocument:
    document = MeetDocument.objects.get(meet_key=meet_key)
    document.space_uri = update_data.space_uri
    document.save()
    return document
