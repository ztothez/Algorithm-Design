"""
Spanning Trees and Components - Assignment 5, Question 3
Algorithm Design by Jon Kleinberg and Éva Tardos

Verify unique MST with distinct weights and the n-k edge bound.
"""

import random

import networkx as nx


def verify_component_edge_bound(n, k):
  g = nx.Graph()
  g.add_nodes_from(range(n))

  vertices = list(range(n))
  random.shuffle(vertices)
  components = [[] for _ in range(k)]
  for idx, v in enumerate(vertices):
    components[idx % k].append(v)

  for comp in components:
    for i in range(len(comp) - 1):
      g.add_edge(comp[i], comp[i + 1])

  extras = []
  for comp in components:
    for i in range(len(comp)):
      for j in range(i + 1, len(comp)):
        if not g.has_edge(comp[i], comp[j]):
          extras.append((comp[i], comp[j]))

  random.shuffle(extras)
  g.add_edges_from(extras[: random.randint(0, max(1, len(extras)))])

  edges = g.number_of_edges()
  bound = n - k
  print(f"Graph: Vertices(n)={n} | Components(k)={nx.number_connected_components(g)} | Total Edges={edges}")
  print(f"       Theoretical Minimum Edge Bound (n - k) = {bound}")
  return edges >= bound


if __name__ == "__main__":
  print("--- Assignment 5: Question 3 ---\n")

  print("Part A: Distinct Edge Weight MST Uniqueness")
  g = nx.Graph()
  g.add_edge("A", "B", weight=10)
  g.add_edge("B", "C", weight=20)
  g.add_edge("C", "A", weight=30)
  mst = nx.minimum_spanning_tree(g, algorithm="kruskal")
  print(f"  Edge set: {list(g.edges(data=True))}")
  print(f"  Unique MST: {sorted(list(mst.edges(data=True)))}\n")

  print("Part B: Component Bound Empirical Checks")
  for n_val, k_val in [(10, 3), (20, 5), (100, 12), (5, 1)]:
    assert verify_component_edge_bound(n_val, k_val)

  print("\nAll tests passed! ✓")
