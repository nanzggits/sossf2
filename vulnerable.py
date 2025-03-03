import sqlite3
from flask import request

def get_user_data():
    user_input = request.args.get('username')
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"  # 🚨 SQL Injection vulnerability!
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()
