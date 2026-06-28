"""
Rumor Propagation - Assignment 3, Question 5
Algorithm Design by Jon Kleinberg and Éva Tardos

Check rumor reachability in an undirected conversation graph (BFS).
"""

from collections import deque


def can_rumor_reach(n, conversations, starter, target):
    """Return True if a rumor from starter can reach target by end of day."""
    if starter == target:
        return True

    adj_list = {f"P_{i}": [] for i in range(1, n + 1)}
    for p1, p2 in conversations:
        adj_list[p1].append(p2)
        adj_list[p2].append(p1)

    visited = {starter}
    queue = deque([starter])

    while queue:
        current = queue.popleft()
        if current == target:
            return True
        for neighbor in adj_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


if __name__ == "__main__":
    print("--- Assignment 3: Question 5 ---\n")

    num_friends = 6
    S = [
        ("P_1", "P_2"),
        ("P_2", "P_3"),
        ("P_4", "P_5"),
        ("P_5", "P_6"),
    ]

    result_a = can_rumor_reach(num_friends, S, "P_1", "P_3")
    print(f"Can rumor spread from P_1 to P_3? {result_a}")
    assert result_a is True

    result_b = can_rumor_reach(num_friends, S, "P_1", "P_6")
    print(f"Can rumor spread from P_1 to P_6? {result_b}")
    assert result_b is False

    print("\nAll tests passed! ✓")
