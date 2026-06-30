"""
Near-Tree MST - Assignment 5, Question 5
Algorithm Design by Jon Kleinberg and Éva Tardos

O(n) MST for near-trees (|E| <= |V| + 8) via cycle elimination.
"""

import collections


def find_cycle_path(tree_adj, start, target):
  queue = collections.deque([[start]])
  visited = {start}
  while queue:
    path = queue.popleft()
    node = path[-1]
    if node == target:
      return path
    for neighbor in tree_adj[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(path + [neighbor])
  return []


def near_tree_mst(vertices, edges):
  adj = {v: [] for v in vertices}
  lookup = {}
  for u, v, w in edges:
    adj[u].append(v)
    adj[v].append(u)
    lookup[tuple(sorted((u, v)))] = w

  visited = {vertices[0]}
  queue = collections.deque([vertices[0]])
  tree_edges = set()
  while queue:
    curr = queue.popleft()
    for neighbor in adj[curr]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
        tree_edges.add(tuple(sorted((curr, neighbor))))

  all_edges = {tuple(sorted((u, v))) for u, v, _ in edges}
  for u, v in all_edges - tree_edges:
    tree_adj = {v: [] for v in vertices}
    for tu, tv in tree_edges:
      tree_adj[tu].append(tv)
      tree_adj[tv].append(tu)

    path = find_cycle_path(tree_adj, u, v)
    cycle = [(u, v)] + [tuple(sorted((path[i], path[i + 1]))) for i in range(len(path) - 1)]
    heaviest = max(cycle, key=lambda e: lookup[e])
    tree_edges.add((u, v))
    tree_edges.remove(heaviest)

  return [(u, v, lookup[(u, v)]) for u, v in tree_edges]


if __name__ == "__main__":
  print("--- Assignment 5: Question 5 ---\n")

  nodes = ["A", "B", "C", "D", "E", "F", "G"]
  edges = [
    ("A", "B", 2), ("B", "C", 4), ("C", "D", 1),
    ("D", "E", 7), ("E", "F", 3), ("F", "G", 8),
    ("G", "A", 9), ("B", "E", 5), ("C", "F", 6),
  ]
  print(f"Vertices n = {len(nodes)}, edges m = {len(edges)} (near-tree: m <= n + 8)\n")

  mst = near_tree_mst(nodes, edges)
  total = sum(w for _, _, w in mst)
  print(f"MST edges: {mst}")
  print(f"Total cost: {total}")

  assert total == 23
  print("\nAll tests passed! ✓")
