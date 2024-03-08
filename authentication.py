import sqlite3

def login(username, password):
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        return True
    else:
        return False

def sign_up(username, password):
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

