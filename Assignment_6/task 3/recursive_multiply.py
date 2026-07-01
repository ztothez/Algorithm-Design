"""
Recursive Integer Multiply - Assignment 6, Question 3
Algorithm Design by Jon Kleinberg and Éva Tardos

Kleinberg-Tardos Recursive-Multiply on 1001_2 x 110_2.
"""


def recursive_multiply(x, y, n):
  if n == 1:
    return x * y

  half = n // 2
  mask = (1 << half) - 1
  x1, x0 = x >> half, x & mask
  y1, y0 = y >> half, y & mask

  x_sum = x1 + x0
  y_sum = y1 + y0
  n_p = max(max(1, x_sum.bit_length()), max(1, y_sum.bit_length()))
  n_p = n if n_p > half else half

  p = recursive_multiply(x_sum, y_sum, n_p)
  x1y1 = recursive_multiply(x1, y1, half)
  x0y0 = recursive_multiply(x0, y0, half)
  return (x1y1 << n) + ((p - x1y1 - x0y0) << half) + x0y0


if __name__ == "__main__":
  print("--- Assignment 6: Question 3 ---\n")

  x, y = int("1001", 2), int("110", 2)
  n = 4
  result = recursive_multiply(x, y, n)

  print(f"Input X: 1001 ({x})")
  print(f"Input Y: 0110 ({y}) [padded to n={n}]")
  print(f"Product (binary): {bin(result)[2:]}")
  print(f"Product (decimal): {result}")

  assert result == 54
  print("\nAll tests passed! ✓")
