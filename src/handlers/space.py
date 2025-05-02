from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse
from src.google_mongo import MeetDocument  # updated name
from src.schemas.space import MeetSpaceSpaceNameUpdate

router = APIRouter()

# READ
@router.get("/space/{meet_key}/space_name", response_model=str)
def get_space_name(meet_key: str):
    space = MeetDocument.objects(meet_key=meet_key).first()
    if not space:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    return space.space_name


# UPDATE
@router.put("/space/{meet_key}/space_name", response_model=str)
def update_space_name(meet_key: str, update: MeetSpaceSpaceNameUpdate):
    space = MeetDocument.objects(meet_key=meet_key).first()
    if not space:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    space.space_name = update.space_name
    space.save()
    return


# DELETE
@router.delete("/space/{meet_key}", response_model=dict)
def delete_space(meet_key: str):
    space = MeetDocument.objects(meet_key=meet_key).first()
    if not space:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    space.delete()
    return {"deleted": True}
