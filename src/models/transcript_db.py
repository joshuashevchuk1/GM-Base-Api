import sqlite3

def init_db():
    with sqlite3.connect('transcripts.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transcripts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT,
                file_data BLOB
            )
        ''')
        conn.commit()

def store_transcript(file_name: str, file_data: bytes):
    with sqlite3.connect('transcripts.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO transcripts (file_name, file_data)
            VALUES (?, ?)
        ''', (file_name, file_data))
        conn.commit()

def get_transcript_by_id(file_id: int):
    with sqlite3.connect('transcripts.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT file_name, file_data FROM transcripts WHERE id = ?', (file_id,))
        return cursor.fetchone()

def list_all_transcripts():
    with sqlite3.connect('transcripts.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, file_name FROM transcripts')
        return cursor.fetchall()
