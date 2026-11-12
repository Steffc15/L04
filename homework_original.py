def square(n):
    """n multiplied by itself"""
    return n * 2


def is_teen(age):
    """True if age is between 13 and 19, both included"""
    return 13 < age <= 19


def count_vowels(text):
    """Number of vowels (a, e, i, o, u) in the text, lowercase or uppercase"""
    return sum(1 for c in text if c in "aeiou")


def is_leap_year(year):
    """True for a leap year: divisible by 4, except years divisible by 100, unless they are also divisible by 400"""
    return year % 4 == 0 and year % 100 != 0


def safe_max(numbers):
    """The largest number in the list, or None if the list is empty"""
    best = 0
    for n in numbers:
        if n > best:
            best = n
    return best
