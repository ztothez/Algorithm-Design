"""
Disk Storage Optimization - Assignment 4, Question 3
Algorithm Design by Jon Kleinberg and Éva Tardos

Smallest-first maximizes program count; largest-first fails on space utilization.
"""


def maximize_program_count(sizes, capacity):
    """Greedy: store smallest programs first."""
    selected = []
    used = 0
    for s in sorted(sizes):
        if used + s <= capacity:
            selected.append(s)
            used += s
        else:
            break
    return selected, used


def maximize_space_greedy_largest(sizes, capacity):
    """Greedy: store largest programs first."""
    selected = []
    used = 0
    for s in sorted(sizes, reverse=True):
        if used + s <= capacity:
            selected.append(s)
            used += s
    return selected, used


def maximize_space_optimal_dp(sizes, capacity):
    """DP reference for maximum disk space used."""
    n = len(sizes)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if sizes[i - 1] <= w:
                dp[i][w] = max(sizes[i - 1] + dp[i - 1][w - sizes[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


if __name__ == "__main__":
    print("--- Assignment 4: Question 3 ---\n")

    programs_a = [40, 10, 20, 15, 30]
    chosen_a, used_a = maximize_program_count(programs_a, 50)
    print(f"Part A — programs {programs_a}, capacity 50 GB")
    print(f"  selected: {chosen_a}, count = {len(chosen_a)}, used = {used_a} GB")

    programs_b = [51, 50, 50]
    greedy_b, used_g = maximize_space_greedy_largest(programs_b, 100)
    optimal_b = maximize_space_optimal_dp(programs_b, 100)
    print(f"\nPart B — programs {programs_b}, capacity 100 GB")
    print(f"  largest-first uses: {used_g} GB")
    print(f"  optimal uses:       {optimal_b} GB")
    assert used_g < optimal_b

    print("\nAll tests passed! ✓")
