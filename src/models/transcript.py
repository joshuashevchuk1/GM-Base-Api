import sqlite3

DB_NAME = 'gm-meet.db'

class Transcript:
    def __init__(self, file_name: str, file_data: bytes, id: int = None):
        self.id = id
        self.file_name = file_name
        self.file_data = file_data

    def save(self):
        """Inserts or updates the transcript in the database."""
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            if self.id is None:
                cursor.execute('''
                    INSERT INTO transcripts (file_name, file_data)
                    VALUES (?, ?)
                ''', (self.file_name, self.file_data))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                    UPDATE transcripts
                    SET file_name = ?, file_data = ?
                    WHERE id = ?
                ''', (self.file_name, self.file_data, self.id))

            conn.commit()

    @staticmethod
    def get_by_id(transcript_id: int):
        """Fetch a transcript by ID."""
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.execute(
                'SELECT id, file_name, file_data FROM transcripts WHERE id = ?',
                (transcript_id,)
            )
            row = cursor.fetchone()
            if row:
                return Transcript(id=row[0], file_name=row[1], file_data=row[2])
            return None

    @staticmethod
    def all():
        """Returns all transcripts as Transcript instances."""
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.execute('SELECT id, file_name, file_data FROM transcripts')
            return [
                Transcript(id=row[0], file_name=row[1], file_data=row[2])
                for row in cursor.fetchall()
            ]

    @staticmethod
    def init_table():
        """Initializes the transcripts table if it doesn't exist."""
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS transcripts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file_name TEXT NOT NULL,
                    file_data BLOB NOT NULL
                )
            ''')
            conn.commit()

    def __repr__(self):
        return f"Transcript(id={self.id}, file_name='{self.file_name}')"