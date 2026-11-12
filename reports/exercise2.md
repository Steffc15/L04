# Bug reports for exercise2.py

Line: 3
Problem: is_passing: returns False for a grade of 5, but the docstring says "5 or more".
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: is_valid_password: checks for length > 8 instead of at least 8 characters, so it fails for exactly 8 characters.
Example: is_valid_password("abcdefg1") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: clamp: uses max(low, min(x, low)) which incorrectly limits x to low twice, resulting in always low or below; should be min(max(x, low), high).
Example: clamp(10, 5, 15) returns 5, expected 10.
Fix: return max(low, min(x, high))
