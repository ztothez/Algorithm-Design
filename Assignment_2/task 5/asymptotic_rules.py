"""
Sum Equals Max Rules - Assignment 2, Question 5
Algorithm Design by Jon Kleinberg and Éva Tardos

Prove sum=max asymptotic rules (a–d) using sympy limit analysis.
"""

import sympy as sp

# Define the symbol n as a positive integer approaching infinity
n = sp.symbols('n', positive=True, real=True)

print("--- Assignment 2: Question 5 Verification ---\n")

# ---------------------------------------------------------
# Part a & c: O(f(n) + g(n)) = O(max(f(n), g(n)))
# ---------------------------------------------------------
print("Evaluating Part a & c (Sum Rule vs Max Rule)...")
# Let's use two arbitrary functions to test the rule
f_n = n**3
g_n = n**2

# The sum of the functions
sum_func = f_n + g_n
# The maximum of the functions (since n->oo, n^3 is the max)
max_func = f_n 

limit_ac = sp.limit(sum_func / max_func, n, sp.oo)
print(f"  Ratio Limit of (f(n)+g(n)) / max(f(n),g(n)) as n->oo: {limit_ac}")
print("  Conclusion: The limit is a constant (1), proving they grow at the exact same rate.")
print("-" * 50)


# ---------------------------------------------------------
# Part b: O(2n^2 log n - 3n + log n + 17) = O(n^2 log n)
# ---------------------------------------------------------
print("Evaluating Part b...")
# Define the complex function and the simplified Big-O function
f_b = 2 * n**2 * sp.log(n) - 3*n + sp.log(n) + 17
g_b = n**2 * sp.log(n)

limit_b = sp.limit(f_b / g_b, n, sp.oo)
print(f"  Ratio Limit of f(n) / g(n) as n->oo: {limit_b}")
print("  Conclusion: TRUE. The limit is a non-zero constant (2), meaning f(n) is Theta(n^2 log n).")
print("-" * 50)


# ---------------------------------------------------------
# Part d: O(n) = O(n + n + ... + n)  [n times]
# ---------------------------------------------------------
print("Evaluating Part d (The Variable Terms Fallacy)...")

# The left side claims the complexity is O(n)
f_d_left = n

# The right side is the sum of n terms, where each term is n.
# Summing 'n' exactly 'n' times equals n * n
f_d_right = n * n 

limit_d = sp.limit(f_d_right / f_d_left, n, sp.oo)
print(f"  Ratio Limit of (n + n + ... n times) / n as n->oo: {limit_d}")
print("  Conclusion: FALSE. The limit approaches infinity.")
print("  Reasoning: The sum evaluates to n^2, which grows strictly faster than n.")
print("             You cannot take the max() when the number of terms being added is a variable.")
print("-" * 50)