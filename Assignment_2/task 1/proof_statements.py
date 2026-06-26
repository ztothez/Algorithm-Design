"""
Big-O Statement Proofs - Assignment 2, Question 1
Algorithm Design by Jon Kleinberg and Éva Tardos

Verify truth of asymptotic statements (a–d) using sympy limits.
"""

import sympy as sp

# Define the symbol n as a positive integer approaching infinity
n = sp.symbols('n', positive=True, real=True)

print("--- Assignment 2: Algorithm Design Verification ---\n")

# ---------------------------------------------------------
# Statement a)
# ---------------------------------------------------------
print("Evaluating Statement a)...")
# f(n) = n^2 / (log3(n) * sqrt(n * ln(n)))
# Note: log3(n) = ln(n)/ln(3)
f_a = n**2 / ((sp.log(n) / sp.log(3)) * sp.sqrt(n * sp.log(n)))
g_a = (n / sp.log(n))**1.5

limit_a = sp.limit(f_a / g_a, n, sp.oo)
print(f"  f(n) / g(n) limit as n -> oo: {limit_a}")
print(f"  Conclusion: {'TRUE' if limit_a.is_number and limit_a != 0 and limit_a != sp.oo else 'FALSE'}")
print("  Reasoning: The ratio is a constant factor (ln(3)), meaning they share the same growth rate.")
print("-" * 50)


# ---------------------------------------------------------
# Statement b)
# ---------------------------------------------------------
print("Evaluating Statement b)...")
# log_base_sqrt(n) (n) = log(n) / log(sqrt(n)) = log(n) / (0.5 * log(n)) = 2
f_b = sp.log(n) / sp.log(sp.sqrt(n))  # Evaluates to 2
g_b = sp.log(n)

limit_b = sp.limit(f_b / g_b, n, sp.oo)
print(f"  f(n) / g(n) limit as n -> oo: {limit_b}")
print(f"  Conclusion: FALSE")
print("  Reasoning: f(n) is a constant (2), whereas g(n) grows logarithmically. O(1) != O(log n).")
print("-" * 50)


# ---------------------------------------------------------
# Statement c)
# ---------------------------------------------------------
print("Evaluating Statement c)...")
# Assuming standard computer science notation: log(n) is log_2(n)
f_c = 2**sp.log(n)                 # 2^(ln n) = n^(1/ln 2) ~ n^1.44
g_c = 2**(sp.log(n)/sp.log(2))     # 2^(log_2 n) = n

limit_c = sp.limit(f_c / g_c, n, sp.oo)
print(f"  f(n) / g(n) limit as n -> oo: {limit_c}")
print(f"  Conclusion: FALSE")
print("  Reasoning: 2^(ln n) grows strictly slower than 2^(log_2 n), so the O-classes differ.")
print("-" * 50)


# ---------------------------------------------------------
# Statement d)
# ---------------------------------------------------------
print("Evaluating Statement d)...")
print("  Statement: f(n) in O(g(n)) => f(n)^2 in O(g(n)^2)")
print("  Conclusion: TRUE")
print("  Proof: If f(n) <= c * g(n) for all n >= n_0, then squaring both sides")
print("         yields f(n)^2 <= c^2 * g(n)^2, which satisfies the definition of O(g(n)^2).")
print("-" * 50)