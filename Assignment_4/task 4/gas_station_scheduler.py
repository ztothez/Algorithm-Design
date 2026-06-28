"""
Gas Station Scheduler - Assignment 4, Question 4
Algorithm Design by Jon Kleinberg and Éva Tardos

Minimize total waiting time with shortest-processing-time-first ordering.
"""

import itertools
import random


def calculate_total_waiting_time(schedule):
    """Sum of completion times for the given service order."""
    total = 0
    elapsed = 0
    for t in schedule:
        elapsed += t
        total += elapsed
    return total


def optimal_gas_station_schedule(service_times):
    """Greedy: sort service times ascending."""
    return sorted(service_times)


if __name__ == "__main__":
    print("--- Assignment 4: Question 4 ---\n")

    random.seed(101)
    car_times = [random.randint(2, 25) for _ in range(7)]
    print(f"Unsorted times: {car_times}")

    greedy_order = optimal_gas_station_schedule(car_times)
    greedy_cost = calculate_total_waiting_time(greedy_order)
    print(f"Greedy order:   {greedy_order}")
    print(f"Greedy total:   {greedy_cost} minutes")

    best_cost = float("inf")
    best_order = None
    for perm in itertools.permutations(car_times):
        cost = calculate_total_waiting_time(perm)
        if cost < best_cost:
            best_cost = cost
            best_order = perm

    print(f"Best order:     {list(best_order)}")
    print(f"Best total:     {best_cost} minutes")
    assert greedy_cost == best_cost
    print("\nAll tests passed! ✓")
