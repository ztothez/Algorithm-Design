"""
Temporal Rumor Propagation - Assignment 3, Question 6
Algorithm Design by Jon Kleinberg and Éva Tardos

Simulate directed rumor spread on a chronologically sorted event stream.
"""


def can_rumor_propagate_temporal(sequence_S, source, start_time, target, deadline):
    """
    Determines if a rumor can travel from 'source' to 'target' by a given 'deadline'
    using a pre-sorted chronological sequence of directed conversations.
    
    Time Complexity: O(m) where m = len(sequence_S)
    Space Complexity: O(n) where n = number of unique friends
    """
    # If the source person is already the target, condition is met instantly
    if source == target and start_time <= deadline:
        return True

    # Keep track of friends who currently know the rumor
    informed_friends = {source}

    # Process triples in chronological order (guaranteed pre-sorted)
    for p_a, p_b, t in sequence_S:
        # Ignore conversations that happened before the rumor even started
        if t < start_time:
            continue
            
        # Stop early if the conversation takes place past our tracking deadline
        if t > deadline:
            break

        # A rumor is passed only if the initiator (p_a) already knows it
        if p_a in informed_friends:
            informed_friends.add(p_b)
            
            # Optimization: If our target has learned the rumor, we can stop
            if p_b == target:
                return True

    return target in informed_friends


# --- Verification & Example Scenarios ---
if __name__ == "__main__":
    print("--- Running Temporal Rumor Propagation Checker (Question 6) ---\n")

    # Sequence S of triples: (Initiator, Recipient, Timestamp)
    # The sequence MUST be pre-sorted by time
    S = [
        ("P_2", "P_3", 10),  # Happens too early (before P_1 starts rumor)
        ("P_1", "P_2", 20),  # P_1 starts conversation, tells P_2
        ("P_3", "P_4", 25),  # P_3 doesn't know it yet, so P_4 hears nothing
        ("P_2", "P_3", 30),  # P_2 knows it and initiates talk with P_3 -> P_3 learns it
        ("P_3", "P_4", 40)   # P_3 now knows it, initiates talk with P_4 -> P_4 learns it
    ]

    rumor_source = "P_1"
    t_start = 15
    
    # Test Case 1: Can P_4 learn it by time 45? (Should be True)
    target_1, deadline_1 = "P_4", 45
    res_1 = can_rumor_propagate_temporal(S, rumor_source, t_start, target_1, deadline_1)
    print(f"Scenario 1: Can rumor reach {target_1} by t={deadline_1}? {res_1}")
    assert res_1 is True, "Verification for Test Case 1 failed!"

    # Test Case 2: Can P_4 learn it by time 35? 
    # (Should be False because P_3 doesn't talk to P_4 until t=40)
    target_2, deadline_2 = "P_4", 35
    res_2 = can_rumor_propagate_temporal(S, rumor_source, t_start, target_2, deadline_2)
    print(f"Scenario 2: Can rumor reach {target_2} by t={deadline_2}? {res_2}")
    assert res_2 is False, "Verification for Test Case 2 failed!"

    print("\nVerification: SUCCESS!")