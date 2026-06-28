"""
Count Shortest Paths - Assignment 3, Question 4
Algorithm Design by Jon Kleinberg and Éva Tardos

Count shortest paths in an unweighted undirected graph via modified BFS.
"""

from collections import deque

def count_shortest_paths(graph, source, target):
    """
    Finds the total number of shortest paths from source to target 
    in an unweighted, undirected graph using an optimized BFS.
    
    Time Complexity: O(m + n)
    Space Complexity: O(n)
    """
    # Initialize distances to infinity and path counts to 0
    dist = {node: float('inf') for node in graph}
    paths = {node: 0 for node in graph}
    
    # Base cases for source vertex
    dist[source] = 0
    paths[source] = 1
    
    # Standard BFS queue initialization
    queue = deque([source])
    
    while queue:
        u = queue.popleft()
        
        # Optimization: if we reach the target, we don't strictly need to process
        # deeper neighbors since any further steps would exceed the minimum distance
        if u == target:
            continue
            
        for neighbor in graph[u]:
            # Case 1: Neighbor discovered for the first time
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[u] + 1
                paths[neighbor] = paths[u]
                queue.append(neighbor)
                
            # Case 2: Another optimal route to this neighbor is found
            elif dist[neighbor] == dist[u] + 1:
                paths[neighbor] += paths[u]
                
    return paths[target]

# --- Verification & Example Demonstration ---
if __name__ == "__main__":
    print("--- Running Shortest Path Counter (Question 4) ---\n")
    
    # Let's construct a symmetric graph with multiple parallel shortest paths
    # Formed like a diamond: A -> B/C -> D -> E/F -> G
    example_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['D', 'G'],
        'F': ['D', 'G'],
        'G': ['E', 'F']
    }
    
    src, dest = 'A', 'G'
    total_paths = count_shortest_paths(example_graph, src, dest)
    
    print(f"Graph structure represents a diamond network from '{src}' to '{dest}'.")
    print(f"Total number of optimal shortest paths: {total_paths}")
    
    # Quick logical trace:
    # A -> B -> D -> E -> G
    # A -> B -> D -> F -> G
    # A -> C -> D -> E -> G
    # A -> C -> D -> F -> G
    # Total paths should equal 4.
    assert total_paths == 4, "Verification failed!"
    print("\nVerification: SUCCESS!")