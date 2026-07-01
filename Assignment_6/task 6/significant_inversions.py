"""
Significant Inversions - Assignment 6, Question 6
Algorithm Design by Jon Kleinberg and Éva Tardos

Count pairs i < j with a_i > 2*a_j in O(n log n) via merge sort.
"""


def count_significant_inversions(arr):
  def divide_and_conquer(a):
    if len(a) <= 1:
      return a, 0

    mid = len(a) // 2
    left, left_c = divide_and_conquer(a[:mid])
    right, right_c = divide_and_conquer(a[mid:])

    cross = 0
    j = 0
    for i in range(len(left)):
      while j < len(right) and left[i] > 2 * right[j]:
        j += 1
      cross += j

    merged = []
    p1 = p2 = 0
    while p1 < len(left) and p2 < len(right):
      if left[p1] <= right[p2]:
        merged.append(left[p1])
        p1 += 1
      else:
        merged.append(right[p2])
        p2 += 1
    merged.extend(left[p1:])
    merged.extend(right[p2:])
    return merged, left_c + right_c + cross

  _, total = divide_and_conquer(arr)
  return total


if __name__ == "__main__":
  print("--- Assignment 6: Question 6 ---\n")

  seq = [13, 3, 5, 1, 20, 6]
  result = count_significant_inversions(seq)

  naive = sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > 2 * seq[j])

  print(f"Sequence: {seq}")
  print(f"Significant inversions: {result}")
  print(f"Naive check: {naive}")

  assert result == naive == 7
  print("\nAll tests passed! ✓")
