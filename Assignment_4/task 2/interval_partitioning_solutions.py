"""
Interval Partitioning - Assignment 4, Question 2
Algorithm Design by Jon Kleinberg and Éva Tardos

Depth formula, else-block demo, and drop-one-interval counterexample.
"""


def compute_depth(intervals):
    """Return maximum number of intervals overlapping at one point."""
    events = []
    for start, finish in intervals:
        events.append((start, 1))
        events.append((finish, -1))

    events.sort(key=lambda x: x[0])

    max_depth = 0
    current = 0
    for _, delta in events:
        current += delta
        max_depth = max(max_depth, current)

    return max_depth


def interval_partitioning_with_limit(intervals, num_labels):
    """Greedy interval partitioning; unlabeled intervals hit the else-block."""
    indexed = [(s, f, i) for i, (s, f) in enumerate(intervals)]
    sorted_intervals = sorted(indexed, key=lambda x: x[0])

    assignments = {}
    unlabeled = []

    for start, finish, inv_id in sorted_intervals:
        excluded = set()
        for ps, pf, pid in sorted_intervals:
            if pid in assignments and start < pf and ps < finish:
                excluded.add(assignments[pid])

        assigned = None
        for label in range(1, num_labels + 1):
            if label not in excluded:
                assigned = label
                break

        if assigned is not None:
            assignments[inv_id] = assigned
        else:
            unlabeled.append((start, finish))

    return assignments, unlabeled


if __name__ == "__main__":
    print("--- Assignment 4: Question 2 ---\n")

    print("Part A: formula-generated intervals")
    n = 10
    intervals_a = [(0.5 * (i - 1), 0.25 * (2 * i + 7)) for i in range(1, n + 1)]
    depth_a = compute_depth(intervals_a)
    print(f"  n = {n}, calculated depth = {depth_a}, expected min(n, 5) = {min(n, 5)}")
    assert depth_a == min(n, 5)

    print("\nPart B: else-block with d = 2 labels")
    overlap = [(0, 2), (0, 2), (0, 2)]
    assignments, unlabeled = interval_partitioning_with_limit(overlap, 2)
    print(f"  assignments: {assignments}")
    print(f"  unlabeled: {unlabeled}")
    assert len(unlabeled) > 0

    print("\nPart C: drop one interval, depth unchanged")
    schedule = [(1, 3)] * 3 + [(7, 9)] * 3
    depth_before = compute_depth(schedule)
    depth_after = compute_depth(schedule[1:])
    print(f"  depth before drop: {depth_before}")
    print(f"  depth after drop:  {depth_after}")
    assert depth_before == depth_after == 3

    print("\nAll tests passed! ✓")
