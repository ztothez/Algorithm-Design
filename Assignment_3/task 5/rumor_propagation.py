"""
Rumor Propagation - Assignment 3, Question 5
Algorithm Design by Jon Kleinberg and Éva Tardos

Check rumor reachability in an undirected conversation graph (BFS).
"""

from collections import deque

def can_rumor_reach(n, conversations, starter, target):
    """
    Determines if a rumor started by 'starter' can reach 'target' 
    given a set of un-timestamped conversations during a day.
    
    Time Complexity: O(n + m) where m = len(conversations)
    Space Complexity: O(n + m)
    """
    # Quick edge case: if the starter is the target, they already know it
    if starter == target:
        return True

    # 1. Build the undirected graph using an adjacency list
    # Friends can be represented as numbers (1 to n) or strings
    adj_list = {}
    
    # Ensure all individuals from 1 to n have an entry in the graph
    for i in range(1, n + 1):
        adj_list[f"P_{i}"] = []
        
    for p1, p2 in conversations:
        adj_list[p1].append(p2)
        adj_list[p2].append(p1)
        
    # 2. Perform BFS traversal to check reachability
    visited = set([starter])
    queue = deque([starter])
    
    while queue:
        current_person = queue.popleft()
        
        # If we have reached the target friend, rumor transmission is possible
        if current_person == target:
            return True
            
        # Spread the rumor to all individuals who conversed with the current person
        for neighbor in adj_list[current_person]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    # If the queue clears without finding the target, it's impossible
    return False


# --- Verification & Example Execution ---
if __name__ == "__main__":
    print("--- Running Rumor Propagation Checker (Question 5) ---\n")
    
    # Imagine a group of 6 friends
    num_friends = 6
    
    # S contains pairs of friends who talked during the day
    # Network path components: (P_1 - P_2 - P_3) and (P_4 - P_5 - P_6)
    S = [
        ("P_1", "P_2"),
        ("P_2", "P_3"),
        ("P_4", "P_5"),
        ("P_5", "P_6"),
    ]
    
    # Scenario A: Can the rumor spread from P_1 to P_3? (Connected component)
    starter_A, target_A = "P_1", "P_3"
    result_A = can_rumor_reach(num_friends, S, starter_A, target_A)
    print(f"Scenario A: Can rumor spread from {starter_A} to {target_A}? {result_A}")
    assert result_A is True, "Verification for Scenario A failed!"
    
    # Scenario B: Can the rumor spread from P_1 to P_6? (Disconnected components)
    starter_B, target_B = "P_1", "P_6"
    result_B = can_rumor_reach(num_friends, S, starter_B, target_B)
    print(f"Scenario B: Can rumor spread from {starter_B} to {target_B}? {result_B}")
    assert result_B is False, "Verification for Scenario B failed!"
    
    print("\nVerification: SUCCESS!")