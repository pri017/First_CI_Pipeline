# First_CI_Pipeline

Assignment 4: Python programs 21-30 with pytest and GitHub Actions.

## Run locally

Use Python 3.12 or newer. From this project folder:

```sh
python -m venv .venv
```

Activate on Windows Command Prompt with `.venv\Scripts\activate`, on
PowerShell with `.venv\Scripts\Activate.ps1`, or on macOS/Linux with
`source .venv/bin/activate`. Then run:

```sh
python -m pip install -r requirements.txt
python -m pytest -v
python codes/21_largest_word.py
```

Every program can also be run directly and prompts for its input. List inputs
use spaces between elements. Numeric list examples accept integers; the
functions also work with appropriate numeric values supplied by tests.

## Programs

| Number | Function | Purpose |
| --- | --- | --- |
| 21 | `largest_word(sentence)` | First longest word, ignoring edge punctuation |
| 22 | `is_anagram(first, second)` | Compare characters ignoring case and spaces |
| 23 | `bubble_sort(numbers)` | Sort a copy using adjacent swaps |
| 24 | `merge_sorted_lists(list1, list2)` | Merge two sorted lists |
| 25 | `find_max_min(numbers)` | Return (maximum, minimum); reject empty input |
| 26 | `sum_of_list(numbers)` | Total elements using a loop |
| 27 | `rotate_list(items, k)` | Rotate a copy right; negative k rotates left |
| 28 | `set_intersection(first, second)` | Return common set elements |
| 29 | `is_armstrong(number)` | Check digit-power sum; negatives are false |
| 30 | `decimal_to_binary(number)` | Repeated division by 2; reject negatives |

The tests use importlib because the required filenames begin with numbers.
The workflow uses the action versions given in the assignment PDF.

## Required GitHub submission sequence

This archive contains the final source files, not evidence of remote CI runs.
Create a repository named `First_CI_Pipeline` (the assignment asks for public).
Clone it and copy the files into the clone, including `.github` and `.gitignore`.
Do not upload the ZIP as a single file. Do not commit a virtual environment.

1. Commit the setup files and Program 21 with its test file; push to `main`.
2. Commit `.github/workflows/python-ci.yml`; push and wait for a successful run.
3. For each program 22 through 30, run all tests, stage only that program and
   its test file, commit, push, and wait for its successful run before the next.
   The local tests will see the remaining uncommitted files; GitHub tests run
   only the files committed at that stage.
4. Take screenshots of the repository file list, Actions runs, and Run tests log.
5. Submit the repository URL and required screenshots.

Example commands for a single program (change filenames and message each time):

```sh
python -m pytest -v
git add codes/22_anagram_strings.py test_cases/test_22_anagram_strings.py
git commit -m "Add program 22: anagram check with tests"
git push origin main
```

Only a completed successful GitHub Actions run proves remote CI success.
