from expense import Expense

import sqlite3

def add_expense(username, amount, description, category):
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO expenses (
                   username,
                   description,
                   amount,
                   category
                   ) VALUES (?, ?, ?, ?)""",
                   (username, description,amount,category)
                   )
    conn.commit()
    conn.close()

def list_expenses(username):
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM expenses WHERE
                   username = ?""",(username,))
    list = cursor.fetchall()
    text = ''
    for row in list:
        text += f'{row[1]} | {row[2]} | {row[3]}\n'
    return text