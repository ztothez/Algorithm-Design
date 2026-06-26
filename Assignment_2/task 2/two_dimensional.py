"""
Matrix Diagonal Counting - Assignment 2, Question 2
Algorithm Design by Jon Kleinberg and Éva Tardos

Count matrix entries on diagonals; benchmark naive vs O(n² log n) approach.
"""

import time
import random
import bisect

def naive_algorithm(B):
    n = len(B)
    A = [0] * n
    for i in range(n):
        c = 0
        for j in range(n):
            for k in range(n):
                if B[j][k] >= B[i][i]:
                    c += 1
        A[i] = c
    return A

def optimized_algorithm(B):
    n = len(B)
    A = [0] * n
    
    # 1. Flatten the 2D matrix into a 1D list: O(n^2)
    flattened = [item for row in B for item in row]
    
    # 2. Sort the 1D list: O(n^2 log(n))
    flattened.sort()
    
    total_elements = n * n
    
    # 3. For each diagonal element, use binary search: O(n log n)
    for i in range(n):
        target = B[i][i]
        # bisect_left finds the first index where element >= target
        idx = bisect.bisect_left(flattened, target)
        A[i] = total_elements - idx
        
    return A

# --- Verification & Performance Benchmark ---
if __name__ == "__main__":
    # Generate a random 150x150 matrix (n = 150)
    # n=150 means n^3 = 3,375,000 operations vs n^2 log(n) ~ 164,000 operations
    n = 150
    matrix = [[random.randint(1, 1000) for _ in range(n)] for _ in range(n)]
    
    print(f"--- Benchmarking with an {n}x{n} Matrix ---")
    
    # Time Naive Algorithm
    start_time = time.time()
    result_naive = naive_algorithm(matrix)
    naive_duration = time.time() - start_time
    print(f"Naive O(n^3) Algorithm Time:      {naive_duration:.5f} seconds")
    
    # Time Optimized Algorithm
    start_time = time.time()
    result_opt = optimized_algorithm(matrix)
    opt_duration = time.time() - start_time
    print(f"Optimized O(n^2 log n) Time:      {opt_duration:.5f} seconds")
    
    # Verify correctness
    assert result_naive == result_opt, "Error: The results do not match!"
    print("\nSuccess: Both algorithms produced identical outputs.")
    print(f"The optimized algorithm is approx {naive_duration / opt_duration:.1f}x faster!")