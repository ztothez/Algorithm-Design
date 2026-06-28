"""
Planar Graph Edge Bound - Assignment 3, Question 2
Algorithm Design by Jon Kleinberg and Éva Tardos

Verify E <= 3|V| - 6 on sample planar and non-planar graphs.
"""

import networkx as nx

def verify_planar_edge_bound(graph, graph_name):
    print(f"Testing {graph_name}:")
    V = graph.number_of_nodes()
    E = graph.number_of_edges()
    
    # Check planarity using NetworkX's built-in Boyer-Myrvold algorithm
    is_planar, _ = nx.check_planarity(graph)
    
    print(f"  Vertices (|V|): {V}")
    print(f"  Edges (|E|):    {E}")
    print(f"  Is Planar?      {is_planar}")
    
    if V >= 3:
        bound = 3 * V - 6
        print(f"  Theoretical Bound (3|V| - 6): {bound}")
        if E <= bound:
            print("  Result: |E| <= 3|V| - 6 holds true.")
        else:
            print("  Result: |E| > 3|V| - 6 violated (As expected, graph cannot be planar).")
            assert not is_planar, "Error: A planar graph broke the theorem!"
    else:
        print("  Condition |V| >= 3 is not met.")
    print("-" * 50)

if __name__ == "__main__":
    print("--- Planar Graph Edge Bound Verification ---\n")
    
    # 1. A standard planar graph: Cycle graph C_5
    g1 = nx.cycle_graph(5)
    verify_planar_edge_bound(g1, "Cycle Graph (C_5)")
    
    # 2. A maximal planar graph: Complete graph K_4
    g2 = nx.complete_graph(4)
    verify_planar_edge_bound(g2, "Complete Graph (K_4)")
    
    # 3. A known non-planar graph: Complete graph K_5
    g3 = nx.complete_graph(5)
    verify_planar_edge_bound(g3, "Complete Non-Planar Graph (K_5)")