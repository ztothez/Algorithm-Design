"""
Dijkstra Negative Edge Failures - Assignment 4, Question 6
Algorithm Design by Jon Kleinberg and Éva Tardos

Show where Dijkstra fails with negative edges and negative cycles.
"""

import heapq


def dijkstra(graph, source):
    """Textbook Dijkstra with finalized visited set."""
    distances = {node: float("inf") for node in graph}
    distances[source] = 0
    pq = [(0, source)]
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


if __name__ == "__main__":
    print("--- Assignment 4: Question 6 ---\n")

    graph_1 = {
        "S": {"A": 1, "B": 3},
        "A": {"C": 2},
        "B": {"A": -3},
        "C": {},
    }
    res_1 = dijkstra(graph_1, "S")
    print("Example 1 - premature finalization")
    print(f"  Dijkstra distances: {res_1}")
    print(f"  True distance to C: 2")
    assert res_1["C"] == 3

    graph_2 = {
        "S": {"A": 1},
        "A": {"B": 1},
        "B": {"A": -3},
    }
    res_2 = dijkstra(graph_2, "S")
    print("\nExample 2 - negative cycle")
    print(f"  Dijkstra distances: {res_2}")
    print(f"  True distance to A: -inf")
    assert res_2["A"] == 1

    print("\nAll tests passed! ✓")
