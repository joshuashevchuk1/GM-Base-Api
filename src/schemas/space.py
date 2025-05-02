from src.google_mongo.model import MeetDocument
from pydantic import BaseModel, Field

class MeetSpaceSpaceNameUpdate(BaseModel):
    space_name: str = Field(..., min_length=1)

# READ
def get_space_name(meet_key: str) -> str:
    space = MeetDocument.objects.get(meet_key=meet_key)
    return space.space_name

# UPDATE
def update_space_name(meet_key: str, update_data: MeetSpaceSpaceNameUpdate) -> MeetDocument:
    space = MeetDocument.objects.get(meet_key=meet_key)
    space.space_name = update_data.space_name
    space.save()
    return space

# DELETE
def delete_meet_space(meet_key: str) -> dict:
    space = MeetDocument.objects.get(meet_key=meet_key)
    space.delete()
    return {"deleted": True}
