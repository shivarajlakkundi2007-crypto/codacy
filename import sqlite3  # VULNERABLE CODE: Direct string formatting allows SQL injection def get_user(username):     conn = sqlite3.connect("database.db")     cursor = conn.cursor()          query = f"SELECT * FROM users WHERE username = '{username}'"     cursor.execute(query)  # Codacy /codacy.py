import sqlite3

# VULNERABLE CODE: Direct string formatting allows SQL injection
def get_user(username):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)  # Codacy / Opengrep will flag this line
    
    return cursor.fetchone()
