"""
Search in Rotated Sorted Array - Assignment 1, Question 3
Algorithm Design by Jon Kleinberg and Éva Tardos

Binary search on a rotated sorted array (pivot find + two-pass search).
"""

S = (1, 2, 4, 6, 10, 11, 14, 19)
S_rotated = (10, 11, 14, 19, 1, 2, 4, 6)


def find_pivot(arr):
  """Return index of the minimum element in a rotated sorted array."""
  low, high = 0, len(arr) - 1
  while low < high:
    mid = (low + high) // 2
    if arr[mid] > arr[high]:
      low = mid + 1
    else:
      high = mid
  return low


def binary_search_range(arr, left, right, k):
  """Standard binary search for k in arr[left:right+1]."""
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == k:
      return True
    if arr[mid] < k:
      left = mid + 1
    else:
      right = mid - 1
  return False


def search_rotated(arr, k):
  """
  Decide whether k exists in a rotated sorted array of distinct integers.
  Time: O(log n) — pivot search plus one binary search.
  """
  n = len(arr)
  if n == 0:
    return False

  pivot = find_pivot(arr)

  if pivot == 0:
    return binary_search_range(arr, 0, n - 1, k)

  if arr[pivot] <= k <= arr[n - 1]:
    return binary_search_range(arr, pivot, n - 1, k)

  if arr[0] <= k <= arr[pivot - 1]:
    return binary_search_range(arr, 0, pivot - 1, k)

  return False


def validate_pivot(arr, pivot_index):
  """Pivot = index of minimum element in a rotated sorted array."""
  n = len(arr)
  if pivot_index < 0 or pivot_index >= n:
    return False
  if arr[pivot_index] != min(arr):
    return False
  if pivot_index > 0 and arr[pivot_index - 1] <= arr[pivot_index]:
    return False
  if pivot_index < n - 1 and arr[pivot_index] >= arr[pivot_index + 1]:
    return False
  return True


if __name__ == "__main__":
  pivot = find_pivot(S_rotated)
  print(f"Pivot found at index: {pivot}")
  print(f"Pivot value: {S_rotated[pivot]}")
  print(f"Is the pivot valid? {validate_pivot(S_rotated, pivot)}")
  print()

  test_values = [1, 6, 10, 19, 3, 7]
  print("Search in rotated array (10, 11, 14, 19, 1, 2, 4, 6):")
  for k in test_values:
    found = search_rotated(S_rotated, k)
    print(f"  k = {k:2d} -> {'found' if found else 'not found'}")

  print()
  print("Search in sorted array (1, 2, 4, 6, 10, 11, 14, 19):")
  for k in test_values:
    found = search_rotated(S, k)
    print(f"  k = {k:2d} -> {'found' if found else 'not found'}")
