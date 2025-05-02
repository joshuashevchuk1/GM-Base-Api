from src.database.model import MeetDocument
from pydantic import BaseModel, Field

class MeetSpaceTopicNameUpdate(BaseModel):
    space_name: str = Field(..., min_length=1)

# READ
def get_space_name(meet_key: str) -> str:
    space = MeetDocument.objects.get(meet_key=meet_key)
    return space.space_name

# UPDATE
def update_space_name(meet_key: str, update_data: MeetSpaceTopicNameUpdate) -> MeetDocument:
    space = MeetDocument.objects.get(meet_key=meet_key)
    space.space_name = update_data.space_name
    space.save()
    return space

