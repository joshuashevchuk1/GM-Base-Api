from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from fastapi.responses import StreamingResponse
import json
import io

from src.models.transcript import Transcript

router = APIRouter()

@router.post("/upload_transcript/")
async def upload_transcript(file: UploadFile = File(...)):
    file_content = await file.read()
    transcript = Transcript(file_name=file.filename, file_data=file_content)
    transcript.save()

    return {"message": "File uploaded successfully", "file_name": transcript.file_name, "id": transcript.id}

@router.get("/get_transcript/{file_id}")
async def get_transcript(
    file_id: int,
    type: str = Query("raw", enum=["raw", "json", "text"], description="Response format: raw, json, or text")
):
    transcript = Transcript.get_by_id(file_id)
    if not transcript:
        raise HTTPException(status_code=404, detail="File not found")

    decoded_data = transcript.file_data.decode("utf-8", errors="replace")

    if type == "json":
        try:
            return {
                "file_name": transcript.file_name,
                "json": json.loads(decoded_data)
            }
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="File is not valid JSON")

    elif type == "text":
        return {
            "file_name": transcript.file_name,
            "text": decoded_data
        }

    # If type=raw, return file for download
    return StreamingResponse(
        io.BytesIO(transcript.file_data),
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={transcript.file_name}"}
    )

@router.get("/list_transcripts/")
async def list_transcripts():
    transcripts = Transcript.all()
    return {
        "transcripts": [
            {"id": t.id, "file_name": t.file_name} for t in transcripts
        ]
    }
