# Bug reports for exercise3.py

Line: 3
Problem: average: returns division by zero for an empty list, but the docstring says an empty list has average 0.
Example: average([]) returns ZeroDivisionError, expected 0.
Fix: return sum(numbers) / (len(numbers) if numbers else 1)

Line: 8
Problem: first_word: returns the first word, but if the text has no words (e.g., only spaces), it returns an empty string, which is correct. However, if the text is empty (""), split() returns [], and [0] raises IndexError. The docstring says "or "" if the text is empty", so it must handle empty string.
Example: first_word("") returns IndexError, expected "".
Fix: return text.split()[0] if text.strip() else ""

Line: 12
Problem: percent: returns division by zero when total is 0, but the docstring says "If total is 0, the result is 0".
Example: percent(5, 0) returns ZeroDivisionError, expected 0.
Fix: return part / total * 100 if total != 0 else 0
