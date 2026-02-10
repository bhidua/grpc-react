import psycopg2
from psycopg2 import DatabaseError
from db import get_connection
import uuid
from datetime import datetime, timezone

def insert_member(name, phone):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO member (member_id, name, phone, last_update)
            VALUES (%s, %s, %s, %s, %s)
        """
        member_id = uuid.uuid4()
        ts = datetime.now(timezone.utc)
        cursor.execute(query, (member_id, name, phone, ts))
        conn.commit()
        print("[SUCCESS] Member inserted")

    except DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"[ERROR] Insert failed: {e}")
        raise

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()