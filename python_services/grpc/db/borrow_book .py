import psycopg2
from psycopg2 import DatabaseError, OperationalError
from db import get_connection
import uuid
from datetime import datetime, timezone

def borrow_book(book_id, member_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # record book is being borrowed 
            # update book for is_available=False
        query = """
            UPDATE book SET is_available = %s WHERE book_id = %s
        """
        ts = datetime.now(timezone.utc)
        cursor.execute(query, (False, book_id))

        # create record of member borrowing book
            # insert record in library_book_transactions
        transaction_id = uuid.uuid4()
        borrowed_time = datetime.now(timezone.utc)
        query = """
            INSERT INTO library_book_transactions (transaction_id, book_id, member_id, borrowed_time)
            VALUES (%s, %s, %s, %s)
        """
        ts = datetime.now(timezone.utc)
        cursor.execute(query, (transaction_id, book_id, member_id, borrowed_time))

        conn.commit()
        print("[SUCCESS] Book Borrowed. Library Book Transaction Created.")
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

def return_book(book_id, member_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # record book is being borrowed 
            # update book for is_available=False
        query = """
            UPDATE book SET is_available = %s WHERE book_id = %s
        """
        ts = datetime.now(timezone.utc)
        cursor.execute(query, (True, book_id))

        # create record of member borrowing book
            # insert record in library_book_transactions
        transaction_id = uuid.uuid4()
        returned_time = datetime.now(timezone.utc)
        query = """
            INSERT INTO library_book_transactions (transaction_id, book_id, member_id, returned_time)
            VALUES (%s, %s, %s, %s)
        """
        ts = datetime.now(timezone.utc)
        cursor.execute(query, (transaction_id, book_id, member_id, returned_time))

        conn.commit()
        print("[SUCCESS] Book Returned. Library Book Transaction Created.")
    except DatabaseError as e:
        if conn:
            conn.rollback()
        print(f"[ERROR] Update failed: {e}")
        raise
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def list_book_borrow_transactions(page=1, page_size=10):
    # ---- input validation ----
    if page < 1:
        raise ValueError("page must be >= 1")
    if page_size < 1 or page_size > 100:
        raise ValueError("page_size must be between 1 and 100")
    offset = (page - 1) * page_size
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # total count (for pagination metadata)
            cur.execute("SELECT COUNT(1) FROM library_book_transactions")
            total = cur.fetchone()[0]

            # paged records
            cur.execute(
                """
                SELECT lt.transaction_id, b.name, m.name, lt.borrowed_time, lt.returned_time
                FROM library_book_transactions lt, book b, member m
                WHERE lt.book_id = b.book_id AND lt.member_id = m.member_id
                ORDER BY lt.borrowed_time desc
                LIMIT %s OFFSET %s
                """,
                (page_size, offset)
            )
            rows = cur.fetchall()

            return {
                "page": page,
                "page_size": page_size,
                "total": total,
                "data": rows
            }
    except (DatabaseError, OperationalError) as db_err:
        conn.rollback()
        raise RuntimeError(f"Database error while fetching library transactions: {db_err}")
    except Exception:
        conn.rollback()
        raise
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
