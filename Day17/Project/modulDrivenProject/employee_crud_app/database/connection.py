import mysql.connector


def get_connection():
    """Create and return a MySQL connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="MicroDegree"
    )
