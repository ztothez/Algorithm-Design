"""
Topological Orderings - Assignment 3, Question 1
Algorithm Design by Jon Kleinberg and Éva Tardos

Enumerate all valid topological sorts for directed graphs (a) and (b).
"""


def find_all_topological_sorts(vertices, edges):
    """
    Finds and returns all possible topological orderings for a given directed graph.
    If the graph contains a cycle, it will return an empty list.
    """
    # 1. Build adjacency list and compute initial in-degrees
    adj = {v: [] for v in vertices}
    in_degree = {v: 0 for v in vertices}
    
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    results = []
    visited = {v: False for v in vertices}
    
    # 2. Backtracking function to explore all permutations
    def backtrack(current_sort):
        # If the current path includes all vertices, a valid ordering is found
        if len(current_sort) == len(vertices):
            results.append(list(current_sort))
            return
        
        for v in vertices:
            # A vertex can be next if it hasn't been visited and its in-degree is 0
            if not visited[v] and in_degree[v] == 0:
                # Include vertex v in the ordering
                visited[v] = True
                current_sort.append(v)
                
                # Decrement in-degree for all its neighbors
                for neighbor in adj[v]:
                    in_degree[neighbor] -= 1
                    
                # Recurse deeper
                backtrack(current_sort)
                
                # Backtrack: undo changes for the next loop iteration
                for neighbor in adj[v]:
                    in_degree[neighbor] += 1
                current_sort.pop()
                visited[v] = False

    backtrack([])
    return results


# --- Graph Configurations from image_174b61.png ---
if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']

    # Graph a) Edges
    edges_a = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'D'), ('C', 'E'),
        ('D', 'F'), ('E', 'F')
    ]

    # Graph b) Edges (Note the bidirectional/cyclic relationship between E and F)
    edges_b = [
        ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'F'),
        ('C', 'B'), ('D', 'B'),
        ('E', 'C'), ('F', 'D'),
        ('E', 'F'), ('F', 'E')  # Cycle here
    ]

    print("--- Assignment 3: Question 1 Results ---\n")

    # Evaluate Graph a
    sorts_a = find_all_topological_sorts(vertices, edges_a)
    print(f"Graph a) Total Topological Orderings: {len(sorts_a)}")
    print("Possibilities:")
    for idx, s in enumerate(sorts_a, 1):
        print(f"  {idx}. {' -> '.join(s)}")
        
    print("\n" + "-"*50 + "\n")

    # Evaluate Graph b
    sorts_b = find_all_topological_sorts(vertices, edges_b)
    print(f"Graph b) Total Topological Orderings: {len(sorts_b)}")
    print("Reasoning:")
    print("  Graph b contains a directed cycle between vertices E and F (E <-> F).")
    print("  Topological sorting is only possible for Directed Acyclic Graphs (DAGs).")
    print("  Therefore, no valid linear ordering can satisfy the constraints.")