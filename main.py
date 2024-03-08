import sqlite3
import app_gui


def initialize_database():
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            username TEXT,
            description TEXT,
            amount REAL,
            category TEXT
        )
    ''')
    conn.commit()
    return conn

def close_database(conn):
    conn.close()

def main():
    # Initialize database connection
    conn = initialize_database()

    # Start GUI
    app = app_gui.App()
    app.mainloop()

    # Close database connection
    close_database(conn)

if __name__ == "__main__":
    main()