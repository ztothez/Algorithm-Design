"""
Judgment Consistency - Assignment 3, Question 7
Algorithm Design by Jon Kleinberg and Éva Tardos

Detect inconsistent same/different judgments via odd-cycle check on contracted graph.
"""

from collections import deque


def is_judgment_consistent(n, same_relations, diff_relations):
    """Return (True/False, short message) for judgment consistency."""
    same_adj = {i: [] for i in range(1, n + 1)}
    for u, v in same_relations:
        same_adj[u].append(v)
        same_adj[v].append(u)

    component_map = {}
    current_cid = 0

    for i in range(1, n + 1):
        if i not in component_map:
            current_cid += 1
            queue = deque([i])
            component_map[i] = current_cid
            while queue:
                curr = queue.popleft()
                for neighbor in same_adj[curr]:
                    if neighbor not in component_map:
                        component_map[neighbor] = current_cid
                        queue.append(neighbor)

    G = {cid: [] for cid in range(1, current_cid + 1)}

    for u, v in diff_relations:
        cid_u = component_map[u]
        cid_v = component_map[v]
        if cid_u == cid_v:
            return False, "inconsistent (same and different on one pair)"
        G[cid_u].append(cid_v)
        G[cid_v].append(cid_u)

    colors = {}
    for cid in range(1, current_cid + 1):
        if cid not in colors:
            queue = deque([cid])
            colors[cid] = 0
            while queue:
                curr = queue.popleft()
                for neighbor in G[curr]:
                    if neighbor not in colors:
                        colors[neighbor] = 1 - colors[curr]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[curr]:
                        return False, "inconsistent (odd cycle)"

    return True, "consistent (no odd cycle)"


if __name__ == "__main__":
    print("--- Assignment 3: Question 7 ---\n")

    res_a, msg_a = is_judgment_consistent(4, [(1, 2), (3, 4)], [(2, 3)])
    print(f"Scenario A: {msg_a}")
    assert res_a is True

    res_b, msg_b = is_judgment_consistent(3, [], [(1, 2), (2, 3), (3, 1)])
    print(f"Scenario B: {msg_b}")
    assert res_b is False

    res_c, msg_c = is_judgment_consistent(2, [(1, 2)], [(1, 2)])
    print(f"Scenario C: {msg_c}")
    assert res_c is False

    print("\nAll tests passed! ✓")
