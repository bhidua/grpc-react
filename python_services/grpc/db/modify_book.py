import psycopg2
from psycopg2 import DatabaseError, OperationalError
from db import get_connection
import uuid
from datetime import datetime, timezone
from book_transaction import book_transaction_pb2

def insert_book(name, author):
    conn = None
    cursor = None
    try:
        print("before getting connection.")
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO book (name, author, last_update,is_available)
            VALUES (%s, %s, %s, %s)
        """
        ts = datetime.now(timezone.utc)
        
        cursor.execute(query, (name, author, ts, True))
        conn.commit()
        print("[SUCCESS] Book inserted")
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

def update_book(book_id, name, author):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            UPDATE book SET name = %s, author = %s, last_update = %s WHERE book_id = %s
        """
        ts = datetime.now(timezone.utc)
        cursor.execute(query, (name, author, ts, book_id))
        conn.commit()
        print("[SUCCESS] Book Updated")
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
    print(f"[list_book_borrow_transactions] connection acquired.")
    try:
        with conn.cursor() as cur:
            # total count (for pagination metadata)
            cur.execute("SELECT COUNT(1) FROM library_book_transactions")
            total = cur.fetchone()[0]
            print(f"[list_book_borrow_transactions] total.{page_size},   {offset}")
            # paged records
            cur.execute(
                """
                SELECT b.name book_name, b.is_available is_available, m.name member_name, lt.borrowed_time btime, lt.returned_time rtime
                FROM library_book_transactions lt, book b, member m
                WHERE lt.book_id = b.book_id AND lt.member_id = m.member_id AND b.is_available=True
                ORDER BY lt.borrowed_time desc
                LIMIT %s OFFSET %s
                """,
                (page_size, offset)
            )
            rows = cur.fetchall()
            print(f"rows: {rows}");
            return book_transaction_pb2.TransactionResponse(
                transactions=[map_book_transaction_row(row) for row in rows]
            )
    except (DatabaseError, OperationalError) as db_err:
        conn.rollback()
        raise RuntimeError(f"Database error while fetching library transactions: {db_err}")
    except Exception as db_exp:
        print(f"exception:  {db_exp}")
        conn.rollback()
        raise
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def list_book_return_transactions(page=1, page_size=10):
    # ---- input validation ----
    if page < 1:
        raise ValueError("page must be >= 1")
    if page_size < 1 or page_size > 100:
        raise ValueError("page_size must be between 1 and 100")
    offset = (page - 1) * page_size
    conn = get_connection()
    print(f"[list_book_borrow_transactions] connection acquired.")
    try:
        with conn.cursor() as cur:
            # total count (for pagination metadata)
            cur.execute("SELECT COUNT(1) FROM library_book_transactions")
            total = cur.fetchone()[0]
            print(f"[list_book_borrow_transactions] total.{page_size},   {offset}")
            # paged records
            cur.execute(
                """
                SELECT b.name book_name, b.is_available is_available, m.name member_name, lt.borrowed_time btime, lt.returned_time rtime
                FROM library_book_transactions lt, book b, member m
                WHERE lt.book_id = b.book_id AND lt.member_id = m.member_id AND b.is_available=False
                ORDER BY lt.borrowed_time desc
                LIMIT %s OFFSET %s
                """,
                (page_size, offset)
            )
            rows = cur.fetchall()
            print(f"rows: {rows}");
            return book_transaction_pb2.TransactionResponse(
                transactions=[map_book_transaction_row(row) for row in rows]
            )
    except (DatabaseError, OperationalError) as db_err:
        conn.rollback()
        raise RuntimeError(f"Database error while fetching library transactions: {db_err}")
    except Exception as db_exp:
        print(f"exception:  {db_exp}")
        conn.rollback()
        raise
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def list_book_all_transactions(page=1, page_size=10):
    # ---- input validation ----
    if page < 1:
        raise ValueError("page must be >= 1")
    if page_size < 1 or page_size > 100:
        raise ValueError("page_size must be between 1 and 100")
    offset = (page - 1) * page_size
    conn = get_connection()
    print(f"[list_book_borrow_transactions] connection acquired.")
    try:
        with conn.cursor() as cur:
            # total count (for pagination metadata)
            cur.execute("SELECT COUNT(1) FROM library_book_transactions")
            total = cur.fetchone()[0]
            print(f"[list_book_borrow_transactions] total.{page_size},   {offset}")
            # paged records
            cur.execute(
                """
                SELECT b.name book_name, b.is_available is_available, m.name member_name, lt.borrowed_time btime, lt.returned_time rtime
                FROM library_book_transactions lt, book b, member m
                WHERE lt.book_id = b.book_id AND lt.member_id = m.member_id
                ORDER BY lt.borrowed_time desc
                LIMIT %s OFFSET %s
                """,
                (page_size, offset)
            )
            rows = cur.fetchall()
            print(f"rows: {rows}");
            return book_transaction_pb2.TransactionResponse(
                transactions=[map_book_transaction_row(row) for row in rows]
            )
    except (DatabaseError, OperationalError) as db_err:
        conn.rollback()
        raise RuntimeError(f"Database error while fetching library transactions: {db_err}")
    except Exception as db_exp:
        print(f"exception:  {db_exp}")
        conn.rollback()
        raise
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def map_book_transaction_row(row):
    print(f"[row found with book name] total.{type(row[3])} " )  
    return book_transaction_pb2.BookTransaction(
        book_name=str(row[0]),
        is_book_available=row[1],
        member_name=row[2],
        borrowed_time=row[3],
        returned_time=row[4]
    )
