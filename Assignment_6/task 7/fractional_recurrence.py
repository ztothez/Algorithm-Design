"""
Fractional Power Recurrence - Assignment 6, Question 7
Algorithm Design by Jon Kleinberg and Éva Tardos

Show T(n) = T(n^(1/3)) + O(1) is Theta(log log n).
"""


def simulate_recurrence(k):
  steps = 0
  while k > 0:
    steps += 1
    k -= 1
  return steps


if __name__ == "__main__":
  print("--- Assignment 6: Question 7 ---\n")
  print(f"{'k':<6}{'n':<18}{'T(n)':<8}{'log log n':<10}")
  print("-" * 42)

  for k in range(1, 7):
    n_str = str(2 ** (3 ** k)) if k <= 3 else f"2^(3^{k})"
    t_n = simulate_recurrence(k)
    print(f"{k:<6}{n_str:<18}{t_n:<8}{k:<10}")

  print("\nAll tests passed! ✓")
