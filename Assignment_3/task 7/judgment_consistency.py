"""
Judgment Consistency - Assignment 3, Question 7
Algorithm Design by Jon Kleinberg and Éva Tardos

Detect inconsistent same/different judgments via odd-cycle check on contracted graph.
"""

from collections import deque


def is_judgment_consistent(n, same_relations, diff_relations):
    """
    Determines if a set of 'same' and 'different' judgments are consistent
    by checking for odd-length cycles in a contracted graph.
    
    Time Complexity: O(m + n)
    Space Complexity: O(m + n)
    """
    # 1. Find connected components using only 'same' edges
    same_adj = {i: [] for i in range(1, n + 1)}
    for u, v in same_relations:
        same_adj[u].append(v)
        same_adj[v].append(u)
        
    component_map = {}
    current_cid = 0
    
    for i in range(1, n + 1):
        if i not in component_map:
            current_cid += 1
            # BFS to mark all nodes in this 'same' component
            queue = deque([i])
            component_map[i] = current_cid
            while queue:
                curr = queue.popleft()
                for neighbor in same_adj[curr]:
                    if neighbor not in component_map:
                        component_map[neighbor] = current_cid
                        queue.append(neighbor)
                        
    # 2. Build the contracted graph G using 'different' edges
    G = {cid: [] for cid in range(1, current_cid + 1)}
    
    for u, v in diff_relations:
        cid_u = component_map[u]
        cid_v = component_map[v]
        
        # If a 'different' relation exists inside the same 'same' component,
        # it forms an odd cycle of length 1 (self-loop) -> Inconsistent
        if cid_u == cid_v:
            return False, "Inconsistent: Contains an odd cycle of length 1 (self-loop)"
            
        G[cid_u].append(cid_v)
        G[cid_v].append(cid_u)
        
    # 3. Check if G contains any odd-length cycles (Bipartiteness check)
    colors = {} # maps component_id to 0 or 1
    
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
                        # Neighbors have the same color -> Odd cycle detected!
                        return False, "Inconsistent: Contains an odd-length cycle"
                        
    return True, "Consistent: No odd cycles found (Graph is bipartite)"

# --- Verification Examples ---
if __name__ == "__main__":
    print("--- Running Judgment Consistency Checker (Question 7) ---\n")
    
    # Scenario A: Consistent judgments
    # 1 == 2, 3 == 4, 2 != 3  => Valid (e.g., Species: {1:A, 2:A, 3:B, 4:B})
    n_A = 4
    same_A = [(1, 2), (3, 4)]
    diff_A = [(2, 3)]
    res_A, msg_A = is_judgment_consistent(n_A, same_A, diff_A)
    print(f"Scenario A: {msg_A}")
    assert res_A is True
    
    # Scenario B: Inconsistent due to an odd cycle of length 3
    # 1 != 2, 2 != 3, 3 != 1 => Triangle (Odd cycle of length 3)
    n_B = 3
    same_B = []
    diff_B = [(1, 2), (2, 3), (3, 1)]
    res_B, msg_B = is_judgment_consistent(n_B, same_B, diff_B)
    print(f"Scenario B: {msg_B}")
    assert res_B is False
    
    # Scenario C: Inconsistent due to a self-loop (Odd cycle of length 1)
    # 1 == 2, but 1 != 2
    n_C = 2
    same_C = [(1, 2)]
    diff_C = [(1, 2)]
    res_C, msg_C = is_judgment_consistent(n_C, same_C, diff_C)
    print(f"Scenario C: {msg_C}")
    assert res_C is False
    print("\nVerification: SUCCESS!")