
import re
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("wukong_memory.db")


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversation_id INTEGER NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (conversation_id)
                    REFERENCES conversations(id)
                    ON DELETE CASCADE
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


# -------------------------
# Conversation management
# -------------------------

def create_conversation(title="New chat"):
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO conversations (title) VALUES (?)",
            (title,),
        )
        return cursor.lastrowid


def list_conversations():
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT id, title, updated_at
            FROM conversations
            ORDER BY updated_at DESC, id DESC
        """).fetchall()

        return [dict(row) for row in rows]


def get_messages(conversation_id):
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT role, content, created_at
            FROM messages
            WHERE conversation_id = ?
            ORDER BY id ASC
        """, (conversation_id,)).fetchall()

        return [dict(row) for row in rows]


def add_message(conversation_id, role, content):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO messages (conversation_id, role, content)
            VALUES (?, ?, ?)
        """, (conversation_id, role, content))

        conn.execute("""
            UPDATE conversations
            SET updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (conversation_id,))


# -------------------------
# Long-term memory
# -------------------------

def add_memory(content):
    content = content.strip()

    if not content:
        return

    with get_connection() as conn:
        conn.execute(
            "INSERT INTO memories (content) VALUES (?)",
            (content,),
        )


def list_memories():
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT id, content, created_at
            FROM memories
            ORDER BY id DESC
        """).fetchall()

        return [dict(row) for row in rows]


def delete_memory(memory_id):
    with get_connection() as conn:
        conn.execute(
            "DELETE FROM memories WHERE id = ?",
            (memory_id,),
        )


def search_memories(query, limit=5):
    """Find memories with words that overlap the user's message."""
    words = set(re.findall(r"\w+", query.lower()))
    words = {word for word in words if len(word) > 2}

    if not words:
        return []

    scored = []

    for memory in list_memories():
        memory_words = set(
            re.findall(r"\w+", memory["content"].lower())
        )

        score = len(words & memory_words)

        if score:
            scored.append((score, memory))

    scored.sort(key=lambda item: item[0], reverse=True)

    return [
        memory for score, memory in scored[:limit]
    ]
