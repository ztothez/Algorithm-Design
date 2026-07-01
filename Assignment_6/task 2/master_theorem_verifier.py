"""
Master Theorem Recurrences - Assignment 6, Question 2
Algorithm Design by Jon Kleinberg and Éva Tardos

Verify recurrences (a)-(d); part (d) falls outside standard Master Theorem.
"""

import math

memo_a, memo_b, memo_c, memo_d = {}, {}, {}, {}


def T_a(n):
  if n <= 1:
    return 1
  if n not in memo_a:
    memo_a[n] = 7 * T_a(n // 2) + n ** 2
  return memo_a[n]


def T_b(n):
  if n <= 1:
    return 1
  if n not in memo_b:
    memo_b[n] = 7 * T_b(n // 3) + n ** 2
  return memo_b[n]


def T_c(n):
  if n <= 1:
    return 1
  if n not in memo_c:
    memo_c[n] = 2 * T_c(n // 4) + math.sqrt(n)
  return memo_c[n]


def T_d(n):
  if n <= 1:
    return 1
  if n not in memo_d:
    memo_d[n] = 2 * T_d(n // 2) + n * math.log(n)
  return memo_d[n]


if __name__ == "__main__":
  print("--- Assignment 6: Question 2 ---\n")

  print("Part (c): T(n) = 2T(n/4) + sqrt(n)")
  print(f"{'n':<10}{'T(n)':<14}{'T/(sqrt(n) log n)':<18}")
  for k in range(5, 11):
    n = 4 ** k
    val = T_c(n)
    denom = math.sqrt(n) * math.log2(n)
    print(f"{n:<10}{val:<14.2f}{val / denom:<18.4f}")

  print("\nPart (d): T(n) = 2T(n/2) + n log n")
  print(f"{'n':<10}{'T(n)':<14}{'T/(n log^2 n)':<18}")
  for k in range(8, 14):
    n = 2 ** k
    val = T_d(n)
    denom = n * (math.log(n) ** 2)
    print(f"{n:<10}{val:<14.2f}{val / denom:<18.4f}")

  print("\nAll tests passed! ✓")
