from itertools import combinations

import matplotlib.pyplot as plt
import networkx as nx

# 1. Define intervals by approximating coordinates (start, end) from the image
# Format: { 'Label': (start, end, row_index) }
intervals = {
    # Row A (y = 4)
    "A1": (0.0, 2.5, 4),
    "A2": (3.5, 6.5, 4),
    "A3": (7.0, 9.5, 4),
    "A4": (10.2, 12.8, 4),
    
    # Row B (y = 3)
    "B1": (0.8, 4.0, 3),
    "B2": (5.0, 7.5, 3),
    "B3": (8.8, 12.2, 3),
    
    # Row C (y = 2)
    "C1": (0.8, 3.2, 2),
    "C2": (3.5, 6.6, 2),
    "C3": (7.2, 9.6, 2),
    "C4": (10.2, 12.8, 2),
    
    # Row D (y = 1)
    "D1": (1.7, 4.8, 1),
    "D2": (5.5, 8.0, 1),
    "D3": (9.0, 11.5, 1)
}

# 2. Build the conflict graph
G = nx.Graph()

# Add all intervals as nodes
for node in intervals:
    G.add_node(node)

# Add an edge if two intervals overlap
keys = list(intervals.keys())
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        u, v = keys[i], keys[j]
        start_u, end_u, _ = intervals[u]
        start_v, end_v, _ = intervals[v]
        
        # Checking for intersection: Max of starts < Min of ends
        if max(start_u, start_v) < min(end_u, end_v):
            G.add_edge(u, v)

# 3. Plot the graph preserving the structural layout
pos = {node: ((data[0] + data[1]) / 2, data[2]) for node, data in intervals.items()}

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Interval Scheduling Encoded as an Independent Set Problem\n(Edges connect overlapping intervals)", fontsize=14, pad=20)

nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', edgecolors='black', ax=ax)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', ax=ax)
nx.draw_networkx_edges(G, pos, width=1.5, edge_color='gray', alpha=0.8, ax=ax)

ax.axis('off')
fig.tight_layout()

# Save once using explicit figure handle
output_path = "independent_set_graph_A.png"
fig.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Graph successfully generated and saved to: {output_path}")

plt.close(fig)

def find_maximum_independent_set(graph):
    """Brute-force maximum independent set (graph is small)."""
    best_set = []
    nodes = list(graph.nodes())
    for size in range(len(nodes) + 1):
        for subset in combinations(nodes, size):
            if all(not graph.has_edge(u, v) for u, v in combinations(subset, 2)):
                if len(subset) > len(best_set):
                    best_set = list(subset)
    return best_set


max_ind_set = find_maximum_independent_set(G)
print(f"Optimal schedule:")
print(sorted(max_ind_set))
print()
print(f"Maximum number of non-overlapping intervals:")
print(len(max_ind_set))