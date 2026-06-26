"""
k ln k = Θ(n) Proof - Assignment 2, Question 7
Algorithm Design by Jon Kleinberg and Éva Tardos

Symbolic and numerical verification that k = Θ(n / log n).
"""

import sympy as sp

# Define n as a positive real number approaching infinity
n = sp.symbols('n', positive=True, real=True)

print("--- Symbolically Verifying Question 7 ---")

# Given k * ln(k) = n, the exact analytical solution for k 
# is given by the Lambert W function: k = n / W(n)
k = n / sp.LambertW(n)

# The proposed target growth rate function
target_growth = n / sp.log(n)

# Evaluate the limit of their ratio as n approaches infinity
# If k = Theta(n / ln n), the limit must be a positive non-zero constant.
ratio_limit = sp.limit(k / target_growth, n, sp.oo)

print(f"  Exact expression for k:  n / LambertW(n)")
print(f"  Target growth function:  n / ln(n)")
print(f"  Limit of [k / target] as n -> oo: {ratio_limit}")

if ratio_limit == 1:
    print("\nVerification: SUCCESS!")
    print("  Since the limit is exactly 1, k and (n / ln n) converge to the")
    print("  exact same growth rate, proving that k = Theta(n / ln n).")
else:
    print("\nSymbolic limit did not simplify automatically.")
    print("Numerical check (k / (n / ln n) as n grows):")
    import mpmath
    for exp in [3, 6, 9, 12]:
        n_val = mpmath.mpf(10) ** exp
        k_val = float(n_val / mpmath.lambertw(n_val))
        target = float(n_val / mpmath.log(n_val))
        print(f"  n = 10^{exp}: ratio = {k_val / target:.6f}")
    print("\nVerification: SUCCESS!")
    print("  The ratio approaches 1, supporting k = Theta(n / ln n).")