# Safe: Using query parameters with placeholders
query = "SELECT * FROM users WHERE username = %s"
cursor.execute(query, (user_input,))
