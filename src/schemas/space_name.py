from src.database.model import MeetDocument
from pydantic import BaseModel, Field

class MeetDocumentSpaceNameUpdate(BaseModel):
    space_name: str = Field(..., min_length=1)

# READ
def get_space_name(meet_key: str) -> str:
    document = MeetDocument.objects.get(meet_key=meet_key)
    return document.space_name

# UPDATE
def update_space_name(meet_key: str, update_data: MeetDocumentSpaceNameUpdate) -> MeetDocument:
    document = MeetDocument.objects.get(meet_key=meet_key)
    document.space_name = update_data.space_name
    document.save()
    return document

