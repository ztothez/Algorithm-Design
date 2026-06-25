# Algorithm Design - Assignment Solutions (Python)
Python implementations for **Algorithm Design** coursework at the University of Turku, based on *Algorithm Design* by Jon Kleinberg and Éva Tardos.

> **Note:** Written proofs and the full assignment report are in `Algorithm Design Assignment Report.md`.

## Requirements
- Python 3.8+
- Tasks 1–4, 6–7: no third-party dependencies
- Task 5 (graph plots): `matplotlib`, `networkx` — use the project `venv`

## Repository structure
```
Assignment 1/
  gale_shapley.py #shared helpers for tasks 2 and 4
  task 1/  Peripatetic_Shipping_Lines.py
  task 2/  G_S_algorithm_v2.py, G_S_algorithm.py
  task 3/  sorted_array.py
  task 4/  truthfulness_gale_shapley.py
  task 5/  Independent_Set_problems_A.py, _B.py, _C.py + graph PNGs
  task 6/  stable_matching_problem.py
  task 7/  same_stable_marriage_instance.py
```

| Task | Question | Script |
|------|----------|--------|
| 1 | Peripatetic Shipping Lines | `task 1/Peripatetic_Shipping_Lines.py` |
| 2 | G-S algorithm (parts a & b) | `task 2/G_S_algorithm_v2.py` |
| 3 | Rotated sorted array search | `task 3/sorted_array.py` |
| 4 | Truthfulness in G-S | `task 4/truthfulness_gale_shapley.py` |
| 5 | Independent Set encodings (a, b, c) | `task 5/Independent_Set_problems_*.py` |
| 6 | Stable matching lemma | `task 6/stable_matching_problem.py` |
| 7 | M″ construction proof | `task 7/same_stable_marriage_instance.py` |

## Usage
Run from the repository root:

```bash
python3 "Assignment 1/task 1/Peripatetic_Shipping_Lines.py"
python3 "Assignment 1/task 2/G_S_algorithm_v2.py"
python3 "Assignment 1/task 3/sorted_array.py"
python3 "Assignment 1/task 4/truthfulness_gale_shapley.py"
./venv/bin/python3 "Assignment 1/task 5/Independent_Set_problems_A.py"
./venv/bin/python3 "Assignment 1/task 5/Independent_Set_problems_B.py"
./venv/bin/python3 "Assignment 1/task 5/Independent_Set_problems_C.py"
python3 "Assignment 1/task 6/stable_matching_problem.py"
python3 "Assignment 1/task 7/same_stable_marriage_instance.py"
```

## References
- Kleinberg, J. & Tardos, É. *Algorithm Design*. Pearson, 2006.
- Gale, D. & Shapley, L. S. (1962). College admissions and the stability of marriage.

## Author
Roosa - University of Turku
