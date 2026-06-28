"""
Interval Scheduling - Assignment 4, Question 1
Algorithm Design by Jon Kleinberg and Éva Tardos

Verify latest-start-time greedy matches earliest-finish-time optimal count.
"""

import random


def schedule_earliest_finish_time(intervals):
    """Greedy by earliest finish time."""
    sorted_intervals = sorted(intervals, key=lambda x: (x[1], x[0]))
    selected = []
    last_finish = float("-inf")

    for start, finish in sorted_intervals:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


def schedule_latest_start_time(intervals):
    """Greedy by latest start time (scan right to left)."""
    sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]), reverse=True)
    selected = []
    last_start = float("inf")

    for start, finish in sorted_intervals:
        if finish <= last_start:
            selected.append((start, finish))
            last_start = start

    return selected[::-1]


if __name__ == "__main__":
    print("--- Assignment 4: Question 1 ---\n")

    random.seed(42)
    mismatches = 0
    num_tests = 1000

    for _ in range(num_tests):
        num_intervals = random.randint(15, 30)
        test_intervals = []
        for _ in range(num_intervals):
            s = random.randint(0, 45)
            f = s + random.randint(2, 10)
            test_intervals.append((s, f))

        if len(schedule_earliest_finish_time(test_intervals)) != len(
            schedule_latest_start_time(test_intervals)
        ):
            mismatches += 1

    print(f"Test runs: {num_tests}")
    print(f"Count mismatches: {mismatches}")
    assert mismatches == 0
    print("\nAll tests passed! ✓")
