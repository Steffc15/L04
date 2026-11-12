import os
import sqlite3
import subprocess

import pytest

import homework
from homework import *


# bug report 1
def test_r1_square_returns_n_squared():
    assert square(3) == 9


# bug report 2
def test_r2_is_teen_includes_13():
    assert is_teen(13) == True


# bug report 3
def test_r3_count_vowels_uppercase():
    assert count_vowels("Apple") == 2


# bug report 4
def test_r4_is_leap_year_2000():
    assert is_leap_year(2000) == True


# bug report 5
def test_r5_safe_max_empty_list():
    assert safe_max([]) == None
