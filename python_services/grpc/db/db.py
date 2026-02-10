import psycopg2
from psycopg2 import OperationalError

def get_connection():
        return psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="admin",
            port=5432
        )