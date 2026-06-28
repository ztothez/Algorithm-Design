"""
Base Station Placement - Assignment 4, Question 5
Algorithm Design by Jon Kleinberg and Éva Tardos

Compare max-coverage greedy vs leftmost-boundary greedy for road coverage.
"""


def base_station_max_coverage(houses, x):
    """Greedy: place a station where it covers the most uncovered houses."""
    uncovered = set(houses)
    stations = []

    while uncovered:
        best_count = -1
        best_pos = None

        for h in houses:
            covered = [u for u in uncovered if abs(u - h) <= x]
            count = len(covered)
            if best_pos is None:
                better = True
            elif count > best_count:
                better = True
            elif count == best_count and (abs(h) < abs(best_pos) or (abs(h) == abs(best_pos) and h < best_pos)):
                better = True
            else:
                better = False
            if better:
                best_count = count
                best_pos = h

        stations.append(best_pos)
        uncovered = {u for u in uncovered if abs(u - best_pos) > x}

    return sorted(stations)


def base_station_optimal(houses, x):
    """Optimal greedy: cover leftmost house by placing station x km to its east."""
    sorted_houses = sorted(houses)
    stations = []
    i = 0
    n = len(sorted_houses)

    while i < n:
        leftmost = sorted_houses[i]
        station_pos = leftmost + x
        stations.append(station_pos)

        while i < n and sorted_houses[i] <= station_pos + x:
            i += 1

    return stations


if __name__ == "__main__":
    print("--- Assignment 4: Question 5 ---\n")

    radius_x = 1.0
    road_houses = [-1.8, -0.9, -0.01, 0, 0.01, 0.9, 1.8]

    print(f"House coordinates: {road_houses}")
    print(f"Coverage radius x: {radius_x} km\n")

    max_cov = base_station_max_coverage(road_houses, radius_x)
    print(f"Max-coverage stations: {max_cov} ({len(max_cov)} total)")

    optimal = base_station_optimal(road_houses, radius_x)
    print(f"Leftmost-boundary stations: {optimal} ({len(optimal)} total)")

    assert len(optimal) < len(max_cov)
    print("\nAll tests passed! ✓")
