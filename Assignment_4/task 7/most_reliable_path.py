"""
Most Reliable Path - Assignment 4, Question 7
Algorithm Design by Jon Kleinberg and Éva Tardos

Maximize path reliability via -ln(r) weights and Dijkstra.
"""

import heapq
import math


def find_most_reliable_path(graph, source, destination):
    """Return (path, reliability) maximizing product of edge reliabilities."""
    transformed = {node: {} for node in graph}
    for u in graph:
        for v, reliability in graph[u].items():
            if reliability > 0:
                transformed[u][v] = -math.log(reliability)

    distances = {node: float("inf") for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0.0
    pq = [(0.0, source)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_node == destination:
            break
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in transformed[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    path = []
    curr = destination
    while curr is not None:
        path.append(curr)
        curr = predecessors[curr]
    path.reverse()

    if distances[destination] == float("inf") or not path or path[0] != source:
        return [], 0.0

    return path, math.exp(-distances[destination])


if __name__ == "__main__":
    print("--- Assignment 4: Question 7 ---\n")

    network = {
        "S": {"A": 0.9, "B": 0.5},
        "A": {"B": 0.95, "C": 0.8},
        "B": {"C": 0.99, "T": 0.6},
        "C": {"T": 0.85},
        "T": {},
    }

    path, reliability = find_most_reliable_path(network, "S", "T")
    print(f"Path: {' -> '.join(path)}")
    print(f"Reliability: {reliability:.4f} ({reliability * 100:.2f}%)")
    assert math.isclose(reliability, 0.7194825)
    print("\nAll tests passed! ✓")
