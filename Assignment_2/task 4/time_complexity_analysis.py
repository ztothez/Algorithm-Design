"""
Range Sum Matrix - Assignment 2, Question 4
Algorithm Design by Jon Kleinberg and Éva Tardos

Build n×n range-sum matrix; benchmark naive O(n²) implementation.
"""

import time
import random

def naive_algorithm(A):
    n = len(A)
    # Initialize n x n matrix with None
    B = [[None for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            # The "Add up" part slices and sums, which takes O(n) time
            B[i][j] = sum(A[i:j+1])
            
    return B

def optimized_algorithm(A):
    n = len(A)
    B = [[None for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        # Anchor the initial element at A[i]
        current_sum = A[i]
        for j in range(i + 1, n):
            # O(1) step: accumulate onto the ongoing range sum
            current_sum += A[j]
            B[i][j] = current_sum
            
    return B

# --- Benchmarking Block ---
if __name__ == "__main__":
    # n=400 means n^3 = 64,000,000 steps vs n^2 = 160,000 steps
    n = 400
    random.seed(42) # Seed fixed for deterministic matrix contents
    array_input = [random.randint(1, 100) for _ in range(n)]
    
    print(f"--- Running Benchmarks for n = {n} ---")
    
    # Measure Naive
    start = time.time()
    res_naive = naive_algorithm(array_input)
    t_naive = time.time() - start
    print(f"Naive Algorithm Theta(n^3) Time:      {t_naive:.5f} seconds")
    
    # Measure Optimized
    start = time.time()
    res_opt = optimized_algorithm(array_input)
    t_opt = time.time() - start
    print(f"Optimized Algorithm O(n^2) Time:      {t_opt:.5f} seconds")
    
    # Verification
    assert res_naive == res_opt, "The output matrices do not match!"
    print(f"\nSuccess! Both matrices match perfectly.")
    print(f"The optimized algorithm runs roughly {t_naive / t_opt:.1f}x faster!")