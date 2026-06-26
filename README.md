# Algorithm Design — Assignment Solutions (Python)

Python implementations for **Algorithm Design** coursework at the University of Turku, based on *Algorithm Design* by Jon Kleinberg and Éva Tardos.

> **Note:** Written proofs and full assignment reports are kept locally (`Algorithm Design Assignment Report.md`, `Algorithm Design Assignment Report 2.md`).

## Requirements

- Python 3.8+
- Most tasks: no third-party dependencies
- Sympy tasks (Assignment 2, Q1/Q3/Q5/Q7): `./venv/bin/python3` after `pip install sympy`
- Graph tasks (Assignment 1, Q5): `matplotlib`, `networkx` — use the project `venv`

## Repository structure

```
Assignment_1/
  gale_shapley.py              # shared helpers for tasks 2 and 4
  task 1/  Peripatetic_Shipping_Lines.py
  task 2/  G_S_algorithm_v2.py, G_S_algorithm.py
  task 3/  sorted_array.py
  task 4/  truthfulness_gale_shapley.py
  task 5/  Independent_Set_problems_A.py, _B.py, _C.py + graph PNGs
  task 6/  stable_matching_problem.py
  task 7/  same_stable_marriage_instance.py

Assignment_2/
  task 1/  proof_statements.py
  task 2/  two_dimensional.py
  task 3/  rigorous.py
  task 4/  time_complexity_analysis.py
  task 5/  asymptotic_rules.py
  task 6/  jar_dropping.py
  task 7/  lambert_verification.py
```

### Assignment 1

| Task | Question | Script |
|------|----------|--------|
| 1 | Peripatetic Shipping Lines | `task 1/Peripatetic_Shipping_Lines.py` |
| 2 | G-S algorithm (parts a & b) | `task 2/G_S_algorithm_v2.py` |
| 3 | Rotated sorted array search | `task 3/sorted_array.py` |
| 4 | Truthfulness in G-S | `task 4/truthfulness_gale_shapley.py` |
| 5 | Independent Set encodings (a, b, c) | `task 5/Independent_Set_problems_*.py` |
| 6 | Stable matching lemma | `task 6/stable_matching_problem.py` |
| 7 | M″ construction proof | `task 7/same_stable_marriage_instance.py` |

### Assignment 2

| Task | Question | Script |
|------|----------|--------|
| 1 | Big-O statement proofs (a–d) | `task 1/proof_statements.py` |
| 2 | Matrix diagonal counting | `task 2/two_dimensional.py` |
| 3 | Asymptotic relations (a–d) | `task 3/rigorous.py` |
| 4 | Range sum matrix (a & b) | `task 4/time_complexity_analysis.py` |
| 5 | Sum/max rules (a–d) | `task 5/asymptotic_rules.py` |
| 6 | Glass jar dropping (a & b) | `task 6/jar_dropping.py` |
| 7 | k ln k = Θ(n) proof | `task 7/lambert_verification.py` |

## Usage

Run from the repository root:

```bash
# Assignment 1
python3 "Assignment_1/task 1/Peripatetic_Shipping_Lines.py"
python3 "Assignment_1/task 2/G_S_algorithm_v2.py"
python3 "Assignment_1/task 3/sorted_array.py"
python3 "Assignment_1/task 4/truthfulness_gale_shapley.py"
./venv/bin/python3 "Assignment_1/task 5/Independent_Set_problems_A.py"
python3 "Assignment_1/task 6/stable_matching_problem.py"
python3 "Assignment_1/task 7/same_stable_marriage_instance.py"

# Assignment 2
./venv/bin/python3 "Assignment_2/task 1/proof_statements.py"
python3 "Assignment_2/task 2/two_dimensional.py"
./venv/bin/python3 "Assignment_2/task 3/rigorous.py"
python3 "Assignment_2/task 4/time_complexity_analysis.py"
./venv/bin/python3 "Assignment_2/task 5/asymptotic_rules.py"
python3 "Assignment_2/task 6/jar_dropping.py"
./venv/bin/python3 "Assignment_2/task 7/lambert_verification.py"
```

## References

- Kleinberg, J. & Tardos, É. *Algorithm Design*. Pearson, 2006.
- Gale, D. & Shapley, L. S. (1962). College admissions and the stability of marriage.

## Author

Roosa Yöruusu — University of Turku
