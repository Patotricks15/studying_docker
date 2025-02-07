from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

app = FastAPI()

@app.get("/")
def read_root():
    """
    Returns a simple hello message.
    """
    return {"message": "Hello, world from FastAPI!"}

@app.get("/db")
def check_db():
    """
    Tries to connect to the MySQL database and returns the server information if successful.
    """
    try:
        connection = mysql.connector.connect(
            host="mysql-db",        # This is the name of the MySQL container on the custom network
            user="root",
            password="my-secret-pw",
            database="testdb",
            port=3306
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            connection.close()
            return {"message": "Connected to MySQL server", "server_info": db_info}
    except Error as e:
        return {"message": "Error connecting to MySQL", "error": str(e)}
