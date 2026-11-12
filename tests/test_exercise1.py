import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even():
    assert is_even(2) == True


# bug report 2
def test_r2_rectangle_area():
    assert rectangle_area(4, 5) == 20


# bug report 3
def test_r3_double_returns_twice_the_number():
    assert double(3) == 6
