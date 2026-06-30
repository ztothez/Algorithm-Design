"""
Linear-Time Kruskal - Assignment 5, Question 4
Algorithm Design by Jon Kleinberg and Éva Tardos

Kruskal with counting sort when weights are integers in [1, |V|].
"""


class DisjointSet:
  def __init__(self, n):
    self.parent = list(range(n))
    self.rank = [0] * n

  def find(self, i):
    if self.parent[i] == i:
      return i
    self.parent[i] = self.find(self.parent[i])
    return self.parent[i]

  def union(self, i, j):
    ri, rj = self.find(i), self.find(j)
    if ri == rj:
      return False
    if self.rank[ri] < self.rank[rj]:
      self.parent[ri] = rj
    elif self.rank[ri] > self.rank[rj]:
      self.parent[rj] = ri
    else:
      self.parent[rj] = ri
      self.rank[ri] += 1
    return True


def optimized_kruskal(num_vertices, edges):
  buckets = [[] for _ in range(num_vertices + 1)]
  for u, v, weight in edges:
    buckets[weight].append((u, v, weight))

  sorted_edges = [e for bucket in buckets for e in bucket]

  dsu = DisjointSet(num_vertices)
  mst = []
  cost = 0
  for u, v, weight in sorted_edges:
    if dsu.union(u, v):
      mst.append((u, v, weight))
      cost += weight
      if len(mst) == num_vertices - 1:
        break
  return mst, cost


if __name__ == "__main__":
  print("--- Assignment 5: Question 4 ---\n")

  v = 5
  edges = [(0, 1, 5), (0, 2, 1), (1, 2, 2), (1, 3, 3), (2, 3, 1), (3, 4, 4), (2, 4, 5)]
  print(f"Vertices |V| = {v}")
  print(f"Edges: {edges}\n")

  mst, total = optimized_kruskal(v, edges)
  print(f"MST edges: {mst}")
  print(f"Total cost: {total}")

  assert total == 8
  print("\nAll tests passed! ✓")
