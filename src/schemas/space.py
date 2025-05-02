from src.google_mongo.model import MeetDocument
from pydantic import BaseModel, Field

# Used for creating a new MeetSpace
class MeetSpaceCreate(BaseModel):
    meet_key: str = Field(..., description="The Google Meet link (unique identifier)")
    space_name: str = Field(..., min_length=1)
    topic_name: str = Field(..., min_length=1)
    space_uri: str = Field(..., min_length=1)

# Used to update only space_name
class MeetSpaceSpaceNameUpdate(BaseModel):
    space_name: str = Field(..., min_length=1)

# Response model
class MeetSpaceResponse(BaseModel):
    meet_key: str
    space_name: str
    topic_name: str
    space_uri: str

# CREATE
def create_meet_space(data: MeetSpaceCreate) -> MeetDocument:
    if MeetDocument.objects(meet_key=data.meet_key).first():
        raise ValueError("Meet key already exists.")
    space = MeetDocument(**data.dict())
    space.save()
    return space

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
