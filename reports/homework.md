# Bug reports for homework.py

Line: 3
Problem: square: returns n * 2 instead of n * n as specified in the docstring.
Example: square(3) returns 6, expected 9.
Fix: return n * n

Line: 8
Problem: is_teen: uses 13 < age <= 19, which excludes 13; the docstring says "both included", so 13 should be True.
Example: is_teen(13) returns False, expected True.
Fix: return 13 <= age <= 19

Line: 13
Problem: count_vowels: only checks lowercase vowels in "aeiou"; the docstring says "lowercase or uppercase", so uppercase vowels (A, E, I, O, U) must also be counted.
Example: count_vowels("Apple") returns 1, expected 2.
Fix: return sum(1 for c in text if c.lower() in "aeiou")

Line: 18
Problem: is_leap_year: incorrectly excludes years divisible by 100 (year % 100 != 0); the docstring says "except years divisible by 100, unless they are also divisible by 400", meaning years divisible by 100 should be leap years if divisible by 400.
Example: is_leap_year(2000) returns False, expected True.
Fix: return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

Line: 23
Problem: safe_max: returns best (initialized to 0) even when the list is empty; the docstring says "or None if the list is empty".
Example: safe_max([]) returns 0, expected None.
Fix: return best if numbers else None
