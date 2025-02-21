```python
import sqlite3
import pickle
import sys

# SQL Injection vulnerability
def get_user_info(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Vulnerable to SQL injection
    cursor.execute(query)
    return cursor.fetchall()

# Unsafe deserialization vulnerability
def load_user_preferences(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)  # Unsafe: Can execute arbitrary code

if __name__ == "__main__":
    user_id = sys.argv[1]
    print(get_user_info(user_id))
```
