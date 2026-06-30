# Algorithm Design - Assignment Solutions (Python)

Python implementations for **Algorithm Design** coursework at the University of Turku, based on *Algorithm Design* by Jon Kleinberg and Éva Tardos.

> **Note:** Written proofs and full assignment reports are kept locally (`Algorithm Design Assignment Report.md` through `Algorithm Design Assignment Report 5.md`).

## Requirements

- Python 3.8+
- Most tasks use only the standard library
- A few tasks need third-party packages (see `requirements.txt`):
  - **sympy** - Assignment 2, tasks 1, 3, 5, 7
  - **networkx**, **matplotlib** - Assignment 1, task 5; Assignment 3, tasks 2 and 3; Assignment 5, tasks 3 and 7

## Setup

The virtual environment is **local only** - `venv/` is in `.gitignore` and is not part of the repository.

From the repository root:

```bash
python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

After activation, use `python3` for all scripts below. Without a venv, only stdlib-only scripts will run.

## Repository structure

```
Assignment_1/
  gale_shapley.py              # shared helpers for tasks 2 and 4
  task 1/  Peripatetic_Shipping_Lines.py
  task 2/  G_S_algorithm_v2.py, G_S_algorithm.py
  task 3/  sorted_array.py
  task 4/  truthfulness_gale_shapley.py
  task 5/  Independent_Set_problems_A.py, _B.py, _C.py
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

Assignment_3/
  task 1/  topological_orderings.py
  task 2/  planar_bounds.py
  task 3/  subgraph_edge_count.py
  task 4/  count_shortest_paths.py
  task 5/  rumor_propagation.py
  task 6/  temporal_rumor_checker.py
  task 7/  judgment_consistency.py

Assignment_4/
  task 1/  interval_scheduling.py
  task 2/  interval_partitioning_solutions.py
  task 3/  disk_storage_optimizer.py
  task 4/  gas_station_scheduler.py
  task 5/  base_station_placement.py
  task 6/  dijkstra_negative_edge_failures.py
  task 7/  most_reliable_path.py

Assignment_5/
  task 1/  robust_network_counterexample.py
  task 2/  havel_hakimi_verifier.py
  task 3/  graph_properties_verifier.py
  task 4/  linear_kruskal.py
  task 5/  near_tree_mst.py
  task 6/  cache_simulator.py
  task 7/  mst_stability.py
```

### Assignment 1


| Task | Question                            | Script                                    |
| ---- | ----------------------------------- | ----------------------------------------- |
| 1    | Peripatetic Shipping Lines          | `task 1/Peripatetic_Shipping_Lines.py`    |
| 2    | G-S algorithm (parts a & b)         | `task 2/G_S_algorithm_v2.py`              |
| 3    | Rotated sorted array search         | `task 3/sorted_array.py`                  |
| 4    | Truthfulness in G-S                 | `task 4/truthfulness_gale_shapley.py`     |
| 5    | Independent Set encodings (a, b, c) | `task 5/Independent_Set_problems_*.py`    |
| 6    | Stable matching lemma               | `task 6/stable_matching_problem.py`       |
| 7    | M″ construction proof               | `task 7/same_stable_marriage_instance.py` |


### Assignment 2


| Task | Question                     | Script                               |
| ---- | ---------------------------- | ------------------------------------ |
| 1    | Big-O statement proofs (a-d) | `task 1/proof_statements.py`         |
| 2    | Matrix diagonal counting     | `task 2/two_dimensional.py`          |
| 3    | Asymptotic relations (a-d)   | `task 3/rigorous.py`                 |
| 4    | Range sum matrix (a & b)     | `task 4/time_complexity_analysis.py` |
| 5    | Sum/max rules (a-d)          | `task 5/asymptotic_rules.py`         |
| 6    | Glass jar dropping (a & b)   | `task 6/jar_dropping.py`             |
| 7    | k ln k = Θ(n) proof          | `task 7/lambert_verification.py`     |


### Assignment 3


| Task | Question                              | Script                             |
| ---- | ------------------------------------- | ---------------------------------- |
| 1    | Topological orderings (graphs a & b)  | `task 1/topological_orderings.py`  |
| 2    | Planar graph edge bound (E <= 3V - 6) | `task 2/planar_bounds.py`          |
| 3    | Vertex-deleted subgraph edge formula  | `task 3/subgraph_edge_count.py`    |
| 4    | Count shortest paths (BFS)            | `task 4/count_shortest_paths.py`   |
| 5    | Rumor propagation (undirected)        | `task 5/rumor_propagation.py`      |
| 6    | Temporal rumor propagation            | `task 6/temporal_rumor_checker.py` |
| 7    | Judgment consistency / odd cycles     | `task 7/judgment_consistency.py`   |


### Assignment 4


| Task | Question                                  | Script                                      |
| ---- | ----------------------------------------- | ------------------------------------------- |
| 1    | Latest-start-time interval scheduling     | `task 1/interval_scheduling.py`             |
| 2    | Interval partitioning (a-c)               | `task 2/interval_partitioning_solutions.py` |
| 3    | Disk storage greedy (a prove, b disprove) | `task 3/disk_storage_optimizer.py`          |
| 4    | Gas pump waiting time (SPT)               | `task 4/gas_station_scheduler.py`           |
| 5    | Base station placement (a & b)            | `task 5/base_station_placement.py`          |
| 6    | Dijkstra negative-edge failures           | `task 6/dijkstra_negative_edge_failures.py` |
| 7    | Most reliable path (-ln + Dijkstra)       | `task 7/most_reliable_path.py`              |


### Assignment 5


| Task | Question                                  | Script                                      |
| ---- | ----------------------------------------- | ------------------------------------------- |
| 1    | Robust network (disprove engineer algo)   | `task 1/robust_network_counterexample.py`   |
| 2    | Havel-Hakimi graphical sequences (a & b)  | `task 2/havel_hakimi_verifier.py`           |
| 3    | Unique MST + component edge bound         | `task 3/graph_properties_verifier.py`       |
| 4    | Linear-time Kruskal (integer weights)     | `task 4/linear_kruskal.py`                  |
| 5    | Near-tree MST in O(n)                     | `task 5/near_tree_mst.py`                   |
| 6    | LRU vs Farthest-in-Future cache (a-c)     | `task 6/cache_simulator.py`                 |
| 7    | MST stable after edge weight decrease     | `task 7/mst_stability.py`                   |


## Usage

Run from the repository root with the venv activated (`source venv/bin/activate`):

```bash
# Assignment 1
python3 "Assignment_1/task 1/Peripatetic_Shipping_Lines.py"
python3 "Assignment_1/task 2/G_S_algorithm_v2.py"
python3 "Assignment_1/task 3/sorted_array.py"
python3 "Assignment_1/task 4/truthfulness_gale_shapley.py"
python3 "Assignment_1/task 5/Independent_Set_problems_A.py"
python3 "Assignment_1/task 5/Independent_Set_problems_B.py"
python3 "Assignment_1/task 5/Independent_Set_problems_C.py"
python3 "Assignment_1/task 6/stable_matching_problem.py"
python3 "Assignment_1/task 7/same_stable_marriage_instance.py"

# Assignment 2
python3 "Assignment_2/task 1/proof_statements.py"
python3 "Assignment_2/task 2/two_dimensional.py"
python3 "Assignment_2/task 3/rigorous.py"
python3 "Assignment_2/task 4/time_complexity_analysis.py"
python3 "Assignment_2/task 5/asymptotic_rules.py"
python3 "Assignment_2/task 6/jar_dropping.py"
python3 "Assignment_2/task 7/lambert_verification.py"

# Assignment 3
python3 "Assignment_3/task 1/topological_orderings.py"
python3 "Assignment_3/task 2/planar_bounds.py"
python3 "Assignment_3/task 3/subgraph_edge_count.py"
python3 "Assignment_3/task 4/count_shortest_paths.py"
python3 "Assignment_3/task 5/rumor_propagation.py"
python3 "Assignment_3/task 6/temporal_rumor_checker.py"
python3 "Assignment_3/task 7/judgment_consistency.py"

# Assignment 4
python3 "Assignment_4/task 1/interval_scheduling.py"
python3 "Assignment_4/task 2/interval_partitioning_solutions.py"
python3 "Assignment_4/task 3/disk_storage_optimizer.py"
python3 "Assignment_4/task 4/gas_station_scheduler.py"
python3 "Assignment_4/task 5/base_station_placement.py"
python3 "Assignment_4/task 6/dijkstra_negative_edge_failures.py"
python3 "Assignment_4/task 7/most_reliable_path.py"

# Assignment 5
python3 "Assignment_5/task 1/robust_network_counterexample.py"
python3 "Assignment_5/task 2/havel_hakimi_verifier.py"
python3 "Assignment_5/task 3/graph_properties_verifier.py"
python3 "Assignment_5/task 4/linear_kruskal.py"
python3 "Assignment_5/task 5/near_tree_mst.py"
python3 "Assignment_5/task 6/cache_simulator.py"
python3 "Assignment_5/task 7/mst_stability.py"
```

## References

- Kleinberg, J. & Tardos, É. *Algorithm Design*. Pearson, 2006.
- Gale, D. & Shapley, L. S. (1962). College admissions and the stability of marriage.

## Author

Roosa Yöruusu - University of Turku