"""
Robust Telecommunication Network - Assignment 5, Question 1
Algorithm Design by Jon Kleinberg and Éva Tardos

Counterexample showing the engineer's double-Kruskal method is not optimal.
"""

import math


class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False


def kruskal(vertices, edges):
    """Return MST edge set as {(u,v): weight, ...} from (weight, u, v) list."""
    uf = UnionFind(vertices)
    mst_edges = {}
    for weight, u, v in sorted(edges, key=lambda x: x[0]):
        if uf.union(u, v):
            edge = (min(u, v), max(u, v))
            mst_edges[edge] = weight
    return mst_edges


def simulate_engineer_algorithm(vertices, geometric_edges):
    weight_lookup = {(min(u, v), max(u, v)): w for w, u, v in geometric_edges}

    t1 = kruskal(vertices, geometric_edges)
    t1_edges = set(t1.keys())
    c = max(weight_lookup.values())

    g_prime = []
    for weight, u, v in geometric_edges:
        edge = (min(u, v), max(u, v))
        new_w = weight + c if edge in t1_edges else weight
        g_prime.append((new_w, u, v))

    t2 = kruskal(vertices, g_prime)
    combined = t1_edges | set(t2.keys())
    total_cost = sum(weight_lookup[e] for e in combined)
    return combined, total_cost


if __name__ == "__main__":
    print("--- Assignment 5: Question 1 ---\n")

    towns = {"A": (0, 1), "B": (-1, 0), "C": (1, 0), "D": (0, -1)}
    vertices = list(towns.keys())

    edges = []
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            u, v = vertices[i], vertices[j]
            x1, y1 = towns[u]
            x2, y2 = towns[v]
            dist = math.hypot(x2 - x1, y2 - y1)
            edges.append((dist, u, v))

    print("Calculated Geometric Edge Costs:")
    for w, u, v in sorted(edges):
        print(f"  Edge ({u}, {v}) -> Cost: {w:.4f}")
    print()

    eng_edges, eng_cost = simulate_engineer_algorithm(vertices, edges)
    optimal_edges = {("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")}
    lookup = {(min(u, v), max(u, v)): w for w, u, v in edges}
    optimal_cost = sum(lookup[e] for e in optimal_edges)

    print("--- Algorithm Analysis Results ---")
    print(f"Engineer's Chosen Network (G''):  {eng_edges}")
    print(f"Engineer's Total Design Cost:     {eng_cost:.4f}")
    print(f"Optimal Perimeter Network (Cycle): {optimal_edges}")
    print(f"True Minimum Robust Design Cost:  {optimal_cost:.4f}")

    assert eng_cost > optimal_cost
    print("\nAll tests passed! ✓")
