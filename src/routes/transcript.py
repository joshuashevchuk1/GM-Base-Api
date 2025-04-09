
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from fastapi.responses import StreamingResponse
import sqlite3
import json
import io

router = APIRouter()

# TODO: clean up and parameterize queries

@router.post("/upload_transcript/")
async def upload_transcript(file: UploadFile = File(...)):
    file_content = await file.read()

    with sqlite3.connect('transcripts.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO transcripts (file_name, file_data) 
            VALUES (?, ?)
        ''', (file.filename, file_content))
        conn.commit()

    return {"message": "File uploaded successfully", "file_name": file.filename}

@router.get("/get_transcript/{file_id}")
async def get_transcript(
    file_id: int,
    type: str = Query("raw", enum=["raw", "json", "text"], description="Response format: raw, json, or text")
):
    with sqlite3.connect('transcripts.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT file_name, file_data FROM transcripts WHERE id = ?', (file_id,))
        file_record = cursor.fetchone()

        if not file_record:
            raise HTTPException(status_code=404, detail="File not found")

        file_name, file_data = file_record
        decoded_data = file_data.decode("utf-8", errors="replace")

        if type == "json":
            try:
                return {
                    "file_name": file_name,
                    "json": json.loads(decoded_data)
                }
            except json.JSONDecodeError:
                raise HTTPException(status_code=400, detail="File is not valid JSON")

        elif type == "text":
            return {
                "file_name": file_name,
                "text": decoded_data
            }

        # If type=raw, return file for download
        return StreamingResponse(
            io.BytesIO(file_data),
            media_type="application/octet-stream",
            headers={"Content-Disposition": f"attachment; filename={file_name}"}
        )

@router.get("/list_transcripts/")
async def list_transcripts():
    with sqlite3.connect('transcripts.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, file_name FROM transcripts')
        files = cursor.fetchall()

    return {"transcripts": [{"id": file[0], "file_name": file[1]} for file in files]}
