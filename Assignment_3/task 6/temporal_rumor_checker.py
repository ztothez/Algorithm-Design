"""
Temporal Rumor Propagation - Assignment 3, Question 6
Algorithm Design by Jon Kleinberg and Éva Tardos

Simulate directed rumor spread on a chronologically sorted event stream.
"""


def can_rumor_propagate_temporal(sequence_S, source, start_time, target, deadline):
    """Return True if source can pass a rumor to target by the deadline."""
    if source == target and start_time <= deadline:
        return True

    informed = {source}

    for p_a, p_b, t in sequence_S:
        if t < start_time:
            continue
        if t > deadline:
            break
        if p_a in informed:
            informed.add(p_b)
            if p_b == target:
                return True

    return target in informed


if __name__ == "__main__":
    print("--- Assignment 3: Question 6 ---\n")

    S = [
        ("P_2", "P_3", 10),
        ("P_1", "P_2", 20),
        ("P_3", "P_4", 25),
        ("P_2", "P_3", 30),
        ("P_3", "P_4", 40),
    ]

    res_1 = can_rumor_propagate_temporal(S, "P_1", 15, "P_4", 45)
    print(f"Can rumor reach P_4 by t=45? {res_1}")
    assert res_1 is True

    res_2 = can_rumor_propagate_temporal(S, "P_1", 15, "P_4", 35)
    print(f"Can rumor reach P_4 by t=35? {res_2}")
    assert res_2 is False

    print("\nAll tests passed! ✓")
