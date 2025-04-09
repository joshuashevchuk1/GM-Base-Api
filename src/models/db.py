import sqlite3


# TODO: parameterize queries
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