import sqlite3
import os

def init_db(db_path):
    """
    Connects to (or creates) the SQLite database, creates a table,
    inserts initial data if the table is empty, and prints all records.
    """
    # Connect to (or create) the SQLite database file
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the 'people' table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Check if the table already has data
    cursor.execute('SELECT COUNT(*) FROM people')
    count = cursor.fetchone()[0]

    # If the table is empty, insert some initial data
    if count == 0:
        cursor.execute("INSERT INTO people (name) VALUES ('Alice')")
        cursor.execute("INSERT INTO people (name) VALUES ('Bob')")
        conn.commit()

    # Retrieve and print all records from the 'people' table
    cursor.execute('SELECT * FROM people')
    rows = cursor.fetchall()
    print("Records in the 'people' table:")
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

if __name__ == '__main__':
    # Create the 'data' directory if it does not exist
    os.makedirs("data", exist_ok=True)
    
    # Define the path to the SQLite database file
    db_path = "data/data.db"
    
    # Initialize the database
    init_db(db_path)
