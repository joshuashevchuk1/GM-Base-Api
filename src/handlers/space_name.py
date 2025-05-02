from fastapi import APIRouter, HTTPException
from src.database import MeetDocument  # updated name
from src.schemas.space_name import MeetDocumentSpaceNameUpdate

router = APIRouter()

# READ space_name by meet_key
@router.get("/document/{meet_key}/space_name", response_model=str, tags=["Space"],)
def get_space_name(meet_key: str):
    space = MeetDocument.objects(meet_key=meet_key).first()
    if not space:
        raise HTTPException(status_code=404, detail="MeetSpace not found")
    return space.space_name


# UPDATE
@router.put("/document/{meet_key}/space_name", response_model=str, tags=["Space"])
def update_space_name(meet_key: str, update: MeetDocumentSpaceNameUpdate):
    space = MeetDocument.objects(meet_key=meet_key).first()
    if not space:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    space.space_name = update.space_name
    space.save()
    return
