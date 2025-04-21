import sqlite3

DB_NAME = 'gm-meet.db'

class ConversationContext:
    def __init__(self, conversation_id: str, user_message: str, bot_response: str, id: int = None, metadata: dict = None):
        self.id = id
        self.conversation_id = conversation_id
        self.user_message = user_message
        self.bot_response = bot_response
        self.metadata = metadata if metadata else {}

    def save(self):
        """Inserts or updates the conversation context in the database."""
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            if self.id is None:
                cursor.execute('''
                    INSERT INTO conversation_context (conversation_id, user_message, bot_response, metadata)
                    VALUES (?, ?, ?, ?)
                ''', (self.conversation_id, self.user_message, self.bot_response, json.dumps(self.metadata)))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                    UPDATE conversation_context
                    SET conversation_id = ?, user_message = ?, bot_response = ?, metadata = ?
                    WHERE id = ?
                ''', (self.conversation_id, self.user_message, self.bot_response, json.dumps(self.metadata), self.id))

            conn.commit()

    @staticmethod
    def get_by_id(context_id: int):
        """Fetch a conversation context by ID."""
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.execute(
                'SELECT id, conversation_id, user_message, bot_response, metadata FROM conversation_context WHERE id = ?',
                (context_id,)
            )
            row = cursor.fetchone()
            if row:
                return ConversationContext(id=row[0], conversation_id=row[1], user_message=row[2], bot_response=row[3], metadata=json.loads(row[4]))
            return None

    @staticmethod
    def get_by_conversation_id(conversation_id: str):
        """Fetch all context for a given conversation ID."""
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.execute(
                'SELECT id, conversation_id, user_message, bot_response, metadata FROM conversation_context WHERE conversation_id = ?',
                (conversation_id,)
            )
            return [
                ConversationContext(id=row[0], conversation_id=row[1], user_message=row[2], bot_response=row[3], metadata=json.loads(row[4]))
                for row in cursor.fetchall()
            ]

    @staticmethod
    def all():
        """Returns all conversation contexts as ConversationContext instances."""
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.execute('SELECT id, conversation_id, user_message, bot_response, metadata FROM conversation_context')
            return [
                ConversationContext(id=row[0], conversation_id=row[1], user_message=row[2], bot_response=row[3], metadata=json.loads(row[4]))
                for row in cursor.fetchall()
            ]

    @staticmethod
    def init_table():
        """Initializes the conversation_context table if it doesn't exist."""
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS conversation_context (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    conversation_id TEXT NOT NULL,
                    user_message TEXT NOT NULL,
                    bot_response TEXT NOT NULL,
                    metadata TEXT
                )
            ''')
            conn.commit()

    def __repr__(self):
        return f"ConversationContext(id={self.id}, conversation_id='{self.conversation_id}', user_message='{self.user_message[:20]}...', bot_response='{self.bot_response[:20]}...')"
