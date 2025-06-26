import psycopg2
from psycopg2 import OperationalError

DB_CONFIG = {
    "dbname": "mydb",
    "user": "myuser",
    "password": "mypassword",
    "host": "192.168.198.173",
    "port": "5432"
}

def get_db_connection():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except OperationalError as e:
        print(f"DB connection error: {e}")
        return None
