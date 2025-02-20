import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Establish and return a database connection."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="bank_db"
        )
        return connection
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None