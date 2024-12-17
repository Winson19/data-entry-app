import sqlite3

def init_db():
    # Connect to SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create a table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT
        )
    ''')

    # Save changes and close connection
    conn.commit()
    conn.close()

# Initialize database
init_db()
