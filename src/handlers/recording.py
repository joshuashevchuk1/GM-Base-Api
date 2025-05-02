from fastapi import APIRouter, HTTPException, UploadFile, File
from src.database import MeetDocument  # Assuming updated name
from io import BytesIO

router = APIRouter()


# Upload a recording
@router.post("/document/{meet_key}/recording", response_model=str, tags=["Recording"])
async def update_recording(meet_key: str, file: UploadFile = File(...)):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")

    file_data = await file.read()

    document.recording.put(BytesIO(file_data), filename=file.filename)
    document.save()

    return "File uploaded successfully"

# Update a recording
@router.put("/document/{meet_key}/recording", response_model=str, tags=["Recording"])
async def update_recording(meet_key: str, file: UploadFile = File(...)):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")

    file_data = await file.read()

    document.recording.replace(BytesIO(file_data), filename=file.filename)
    document.save()

    return "File uploaded successfully"


# Retrieve the uploaded recording
@router.get("/document/{meet_key}/recording", tags=["Recording"])
async def get_file(meet_key: str):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")

    if document.recording:
        return document.recording.read()  # Return the file content
    else:
        raise HTTPException(status_code=404, detail="recording file not found")

# Delete the uploaded recording
@router.delete("/document/{meet_key}/recording", response_model=str, tags=["Recording"])
async def delete_recording(meet_key: str):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")

    if not document.recording:
        raise HTTPException(status_code=404, detail="recording file not found")

    document.recording.delete()
    document.recording = None
    document.save()

    return "recording deleted successfully"
