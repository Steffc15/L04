# Bug reports for exercise4.py

Line: 4
Problem: ADMIN_PASSWORD is hardcoded as "admin123" in the source code, which is a security vulnerability. The docstring does not specify a secret, but the function check_admin relies on this secret. According to security best practices, secrets should never be hardcoded and should instead be read from environment variables. The presence of the secret in the source code exposes it to version control and potential exposure.
Example: The secret "admin123" is visible in the source code, expected to be absent.
Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")

Line: 14
Problem: The function find_user uses string concatenation in an f-string to build an SQL query with user input, making it vulnerable to SQL injection attacks. The docstring states it returns the user's row or None if the username does not exist, but it does not specify safe handling of user input. Using f-strings with user input directly in SQL queries allows attackers to inject malicious SQL code.
Example: find_user(db, "x' OR '1'='1") returns a row, expected None.
Fix: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
