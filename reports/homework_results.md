# Homework results: homework.py

| # | Function | Difficulty | Planted bug | Bug report (line) | Test (test-writer) | Test on original | Test on fixed | Reference check on fixed |
|---|---|---|---|---|---|---|---|---|
| 1 | `square` | 1 - easy | n * 2 instead of n * n | yes (line 3) | test_r1_square_returns_n_squared | FAIL | PASS | PASS |
| 2 | `is_teen` | 2 - easy | 13 < age: 13 is not included | yes (line 8) | test_r2_is_teen_includes_13 | FAIL | PASS | PASS |
| 3 | `count_vowels` | 3 - medium | uppercase vowels are not counted | yes (line 13) | test_r3_count_vowels_uppercase | FAIL | PASS | PASS |
| 4 | `is_leap_year` | 4 - medium | the 'divisible by 400' rule is missing | yes (line 18) | test_r4_is_leap_year_2000 | FAIL | PASS | PASS |
| 5 | `safe_max` | 5 - hard | 2 bugs: [] gives 0, all-negative lists give 0 | yes (line 23) | test_r5_safe_max_empty_list | FAIL | PASS | **FAIL** |

**Fully solved: 4/5** (bug found, test fails on the original, passes on the fix, and the fix passes my reference check)
