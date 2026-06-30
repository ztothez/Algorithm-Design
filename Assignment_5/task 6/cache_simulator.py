"""
Cache Replacement - Assignment 5, Question 6
Algorithm Design by Jon Kleinberg and Éva Tardos

Compare LRU and Farthest-in-Future (Belady) on the assignment sequence.
"""


def simulate_lru(sequence, capacity):
  cache = []
  misses = 0
  for item in sequence:
    if item in cache:
      cache.remove(item)
      cache.append(item)
    else:
      misses += 1
      if len(cache) >= capacity:
        cache.pop(0)
      cache.append(item)
  return misses


def simulate_ff(sequence, capacity):
  cache = set()
  misses = 0
  for i, item in enumerate(sequence):
    if item in cache:
      continue
    misses += 1
    if len(cache) < capacity:
      cache.add(item)
      continue
    farthest_idx = -1
    evict = None
    for cached in cache:
      try:
        nxt = sequence.index(cached, i + 1)
      except ValueError:
        nxt = float("inf")
      if nxt > farthest_idx:
        farthest_idx = nxt
        evict = cached
    cache.remove(evict)
    cache.add(item)
  return misses


if __name__ == "__main__":
  print("--- Assignment 5: Question 6 ---\n")

  seq = ["a", "b", "c", "b", "a", "d", "a", "e", "b", "e", "c", "f", "d"]

  print("Part A: cache size k = 3")
  lru_3 = simulate_lru(seq, 3)
  ff_3 = simulate_ff(seq, 3)
  print(f"  LRU misses: {lru_3}")
  print(f"  FF misses:  {ff_3}\n")

  print("Part B: scanning capacities")
  print(f"{'k':<6}{'LRU':<8}{'FF':<8}{'Match'}")
  matches = []
  for k in range(1, 8):
    lru_m = simulate_lru(seq, k)
    ff_m = simulate_ff(seq, k)
    ok = lru_m == ff_m
    if ok:
      matches.append(k)
    print(f"{k:<6}{lru_m:<8}{ff_m:<8}{'yes' if ok else 'no'}")

  assert lru_3 == 9 and ff_3 == 7
  assert matches == [1, 2, 6, 7]
  print("\nAll tests passed! ✓")
