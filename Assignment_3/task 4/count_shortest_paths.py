"""
Count Shortest Paths - Assignment 3, Question 4
Algorithm Design by Jon Kleinberg and Éva Tardos

Count shortest paths in an unweighted undirected graph via modified BFS.
"""

from collections import deque


def count_shortest_paths(graph, source, target):
    """Return the number of shortest paths from source to target."""
    dist = {node: float('inf') for node in graph}
    paths = {node: 0 for node in graph}

    dist[source] = 0
    paths[source] = 1
    queue = deque([source])

    while queue:
        u = queue.popleft()
        if u == target:
            continue

        for neighbor in graph[u]:
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[u] + 1
                paths[neighbor] = paths[u]
                queue.append(neighbor)
            elif dist[neighbor] == dist[u] + 1:
                paths[neighbor] += paths[u]

    return paths[target]


if __name__ == "__main__":
    print("--- Assignment 3: Question 4 ---\n")

    example_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['D', 'G'],
        'F': ['D', 'G'],
        'G': ['E', 'F'],
    }

    src, dest = 'A', 'G'
    total_paths = count_shortest_paths(example_graph, src, dest)

    print(f"Diamond graph from {src} to {dest}")
    print(f"Shortest paths found: {total_paths}")

    assert total_paths == 4
    print("\nAll tests passed! ✓")
