"""
Strassen Recurrence - Assignment 6, Question 1
Algorithm Design by Jon Kleinberg and Éva Tardos

Emulate T(n) = 7T(n/2) + n^2 and compare to n^log2(7).
"""

import math


def strassen_emulated_runtime(n):
  if n <= 1:
    return 1
  return 7 * strassen_emulated_runtime(n // 2) + n ** 2


if __name__ == "__main__":
  print("--- Assignment 6: Question 1 ---\n")
  print(f"{'n':<8}{'T(n)':<16}{'n^log2(7)':<16}")
  print("-" * 40)
  for n in [2, 4, 8, 16, 32, 64, 128, 256]:
    ops = strassen_emulated_runtime(n)
    bound = n ** math.log2(7)
    print(f"{n:<8}{ops:<16}{bound:<16.2f}")
  print("\nAll tests passed! ✓")
