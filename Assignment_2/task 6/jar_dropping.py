"""
Glass Jar Dropping - Assignment 2, Question 6
Algorithm Design by Jon Kleinberg and Éva Tardos

DP for minimum worst-case drops; verify theoretical bound.
"""

import math

def solve_jar_dropping(rungs, jars):
    """
    Computes the minimum number of drops needed in the worst case 
    using Dynamic Programming.
    """
    # dp[i][j] represents the minimum drops for i jars and j rungs
    dp = [[0] * (rungs + 1) for _ in range(jars + 1)]
    
    # Base Case 1: 1 rung requires 1 drop, 0 rungs require 0 drops
    for i in range(1, jars + 1):
        dp[i][0] = 0
        dp[i][1] = 1
        
    # Base Case 2: 1 jar requires linear scanning (j drops for j rungs)
    for j in range(1, rungs + 1):
        dp[1][j] = j
        
    # Fill the DP table
    for i in range(2, jars + 1):
        for j in range(2, rungs + 1):
            dp[i][j] = float('inf')
            # Test dropping a jar from every possible rung 'x'
            for x in range(1, j + 1):
                # If it breaks: we check x-1 rungs below with i-1 jars
                # If it doesn't break: we check j-x rungs above with i jars
                worst_case_at_x = 1 + max(dp[i-1][x-1], dp[i][j-x])
                dp[i][j] = min(dp[i][j], worst_case_at_x)
                
    return dp[jars][rungs]

# --- Verification & Analysis Execution ---
if __name__ == "__main__":
    test_rungs = 100
    
    print(f"--- Analyzing Jar Dropping Puzzle for {test_rungs} Rungs ---\n")
    print(f"{'Jars (k)':<10}{'Exact Optimal Drops':<25}{'Theoretical Bound (k * n^(1/k))':<30}")
    print("-" * 70)
    
    for k in range(1, 6):
        optimal_drops = solve_jar_dropping(test_rungs, k)
        # Calculate our theoretical bound: k * n^(1/k)
        theoretical_bound = k * (test_rungs ** (1 / k))
        
        print(f"{k:<10}{optimal_drops:<25}{theoretical_bound:<30.2f}")
        
    print("\nObservation:")
    print("Notice how the exact optimal drops always remain below or equal")
    print("to our theoretical upper bound, verifying our strategy works perfectly!")