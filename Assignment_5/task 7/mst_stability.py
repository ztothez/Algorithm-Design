"""
MST Stability Under Decrease - Assignment 5, Question 7
Algorithm Design by Jon Kleinberg and Éva Tardos

Verify MST edge set unchanged after decreasing one tree edge weight.
"""

import networkx as nx


if __name__ == "__main__":
  print("--- Assignment 5: Question 7 ---\n")

  g = nx.Graph()
  for u, v, w in [
    ("A", "B", 4), ("B", "C", 8), ("C", "D", 7),
    ("D", "E", 9), ("E", "F", 10), ("F", "G", 2),
    ("G", "H", 1), ("H", "A", 8), ("B", "H", 11),
    ("C", "I", 2), ("G", "I", 6), ("H", "I", 7),
  ]:
    g.add_edge(u, v, weight=w)

  initial = nx.minimum_spanning_tree(g, algorithm="kruskal")
  initial_edges = sorted(tuple(sorted(e)) for e in initial.edges())
  print(f"Initial MST: {initial_edges}")

  target = ("C", "I")
  decrease = 1.5
  print(f"Decrease {target} by {decrease}")

  g[target[0]][target[1]]["weight"] -= decrease
  updated = nx.minimum_spanning_tree(g, algorithm="kruskal")
  updated_edges = sorted(tuple(sorted(e)) for e in updated.edges())
  print(f"MST after decrease: {updated_edges}")

  assert initial_edges == updated_edges
  print("\nAll tests passed! ✓")
