"""
Grid Local Minimum - Assignment 6, Question 5
Algorithm Design by Jon Kleinberg and Éva Tardos

Find a local minimum in an n x n grid using O(n) probes.
"""

import random


def find_local_minimum(matrix):
  n = len(matrix)
  probed = {}
  probe_count = [0]

  def probe(r, c):
    if not (0 <= r < n and 0 <= c < n):
      return float("inf")
    if (r, c) not in probed:
      probed[(r, c)] = matrix[r][c]
      probe_count[0] += 1
    return probed[(r, c)]

  def solve(r_start, r_end, c_start, c_end, entry_node=None):
    if r_start > r_end or c_start > c_end:
      return entry_node

    r_mid = (r_start + r_end) // 2
    c_mid = (c_start + c_end) // 2
    best_node = entry_node
    best_val = matrix[entry_node[0]][entry_node[1]] if entry_node else float("inf")

    for c in range(c_start, c_end + 1):
      val = probe(r_mid, c)
      if val < best_val:
        best_val = val
        best_node = (r_mid, c)

    for r in range(r_start, r_end + 1):
      val = probe(r, c_mid)
      if val < best_val:
        best_val = val
        best_node = (r, c_mid)

    r_b, c_b = best_node
    is_local_min = True
    smallest_neighbor = None
    smallest_neighbor_val = best_val

    for nr, nc in [(r_b - 1, c_b), (r_b + 1, c_b), (r_b, c_b - 1), (r_b, c_b + 1)]:
      if 0 <= nr < n and 0 <= nc < n:
        n_val = probe(nr, nc)
        if n_val < best_val:
          is_local_min = False
          if n_val < smallest_neighbor_val:
            smallest_neighbor_val = n_val
            smallest_neighbor = (nr, nc)

    if is_local_min:
      return r_b, c_b

    nr, nc = smallest_neighbor
    if nr < r_mid:
      if nc < c_mid:
        return solve(r_start, r_mid - 1, c_start, c_mid - 1, smallest_neighbor)
      return solve(r_start, r_mid - 1, c_mid + 1, c_end, smallest_neighbor)
    if nc < c_mid:
      return solve(r_mid + 1, r_end, c_start, c_mid - 1, smallest_neighbor)
    return solve(r_mid + 1, r_end, c_mid + 1, c_end, smallest_neighbor)

  r_min, c_min = solve(0, n - 1, 0, n - 1)
  return r_min, c_min, probe_count[0]


if __name__ == "__main__":
  print("--- Assignment 6: Question 5 ---\n")

  random.seed(42)
  grid_size = 100
  nums = list(range(1, grid_size * grid_size + 1))
  random.shuffle(nums)
  grid = [nums[i * grid_size : (i + 1) * grid_size] for i in range(grid_size)]

  r_min, c_min, probes = find_local_minimum(grid)
  val = grid[r_min][c_min]

  print(f"Grid: {grid_size} x {grid_size}")
  print(f"Local minimum: row {r_min}, col {c_min}, value {val}")
  print(f"Probes used: {probes} (bound 4n = {4 * grid_size})")

  neighbors = []
  if r_min > 0:
    neighbors.append(grid[r_min - 1][c_min])
  if r_min < grid_size - 1:
    neighbors.append(grid[r_min + 1][c_min])
  if c_min > 0:
    neighbors.append(grid[r_min][c_min - 1])
  if c_min < grid_size - 1:
    neighbors.append(grid[r_min][c_min + 1])

  assert all(val < n for n in neighbors)
  assert probes <= 4 * grid_size
  print("\nAll tests passed! ✓")
