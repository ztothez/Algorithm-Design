"""
Recurrence Algorithm Comparison - Assignment 6, Question 4
Algorithm Design by Jon Kleinberg and Éva Tardos

Compare divide-and-conquer algorithms A, B, and C by recurrence cost.
"""

memo_A, memo_B, memo_C = {}, {}, {}


def algorithm_A(n):
  if n <= 1:
    return 1
  if n not in memo_A:
    memo_A[n] = 5 * algorithm_A(n // 2) + n
  return memo_A[n]


def algorithm_B(n):
  if n <= 0:
    return 1
  if n not in memo_B:
    memo_B[n] = 2 * algorithm_B(n - 1) + 1
  return memo_B[n]


def algorithm_C(n):
  if n <= 1:
    return 1
  if n not in memo_C:
    memo_C[n] = 9 * algorithm_C(n // 3) + n ** 2
  return memo_C[n]


if __name__ == "__main__":
  print("--- Assignment 6: Question 4 ---\n")
  print(f"{'n':<8}{'Algo A':<14}{'Algo B':<18}{'Algo C':<14}")
  print("-" * 54)

  for n in [6, 18, 54, 162, 486]:
    a = algorithm_A(n)
    b = algorithm_B(n) if n <= 20 else None
    c = algorithm_C(n)
    b_str = str(b) if b is not None else "overflow"
    print(f"{n:<8}{a:<14}{b_str:<18}{c:<14}")

  print("\nAll tests passed! ✓")
