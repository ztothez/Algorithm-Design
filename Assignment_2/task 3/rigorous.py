"""
Asymptotic Relations - Assignment 2, Question 3
Algorithm Design by Jon Kleinberg and Éva Tardos

Determine O, Ω, Θ relationships between f(n) and g(n) using sympy.
"""

import sympy as sp

# Define symbols
n = sp.symbols('n', positive=True, real=True)
k = sp.symbols('k', positive=True, real=True)

def determine_asymptotic_relation(f, g, context_str):
    print(f"Evaluating {context_str}...")
    # Calculate the limit of the ratio f(n) / g(n) as n goes to infinity
    ratio_limit = sp.limit(f / g, n, sp.oo)
    
    if ratio_limit == 0:
        print("  Result: f(n) = O(g(n))  [g(n) grows strictly faster]")
    elif ratio_limit == sp.oo:
        print("  Result: f(n) = Omega(g(n))  [f(n) grows strictly faster]")
    else:
        print(f"  Result: f(n) = Theta(g(n))  [Same growth rate, limit = {ratio_limit}]")
    print("-" * 50)

# --- a) ---
f_a = 10*n + sp.log(n**2)
g_a = (1/2)*n + (sp.log(n))**2
determine_asymptotic_relation(f_a, g_a, "Part a")

# --- b) ---
f_b = (n**2) * sp.log(n)
g_b = 6**(2 * sp.log(n) / sp.log(3)) # log3(n) written as log(n)/log(3)
determine_asymptotic_relation(f_b, g_b, "Part b")

# --- c) ---
f_c = n * (2**n)
g_c = 3**n
determine_asymptotic_relation(f_c, g_c, "Part c")

# --- d) ---
# Sum of i^k approximated asymptotically as (n^(k+1)) / (k+1)
f_d = (n**(k + 1)) / (k + 1)
g_d = n**(k + 1)
determine_asymptotic_relation(f_d, g_d, "Part d")