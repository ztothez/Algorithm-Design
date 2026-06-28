"""
Vertex-Deleted Subgraph Edge Formula - Assignment 3, Question 3
Algorithm Design by Jon Kleinberg and Éva Tardos

Verify vertex-deleted subgraph edge-count formula on test graphs.
"""

import networkx as nx

def verify_subgraph_edge_formula(G, graph_name):
    """
    Computes the RHS of the formula from image_18345f.png 
    and checks if it matches the total edge count |E|.
    """
    n = G.number_of_nodes()
    total_edges = G.number_of_edges()
    
    sum_subgraph_edges = 0
    
    # Iterate through every vertex, copy the graph, delete the vertex, 
    # and sum up the remaining edges.
    for v in G.nodes():
        G_minus_v = G.copy()
        G_minus_v.remove_node(v)
        sum_subgraph_edges += G_minus_v.number_of_edges()
        
    # Calculate the Right-Hand Side (RHS) of the formula
    rhs_value = sum_subgraph_edges / (n - 2)
    
    print(f"Testing {graph_name}:")
    print(f"  Total Vertices (|V_G|):           {n}")
    print(f"  Total Expected Edges (|E|):       {total_edges}")
    print(f"  Sum of all |E_(G-v)| subgraphs:   {sum_subgraph_edges}")
    print(f"  Calculated RHS {sum_subgraph_edges} / ({n} - 2) =  {rhs_value}")
    print(f"  Formula Verified?                 {total_edges == rhs_value}")
    print("-" * 60)
    
    return total_edges == rhs_value

if __name__ == "__main__":
    print("--- Verification of Vertex-Deleted Subgraph Edge Formula ---\n")
    
    # Test 1: Complete Graph K_4 (4 nodes, 6 edges)
    g_complete = nx.complete_graph(4)
    verify_subgraph_edge_formula(g_complete, "Complete Graph (K_4)")
    
    # Test 2: Cycle Graph C_5 (5 nodes, 5 edges)
    g_cycle = nx.cycle_graph(5)
    verify_subgraph_edge_formula(g_cycle, "Cycle Graph (C_5)")
    
    # Test 3: Erdős-Rényi Random Graph (7 nodes, edge probability 0.5)
    g_random = nx.gnp_random_graph(7, 0.5, seed=123)
    verify_subgraph_edge_formula(g_random, "Random Graph (G_n,p)")