from itertools import combinations
import matplotlib.pyplot as plt
import networkx as nx

# 1. Define intervals by approximating coordinates (start, end) and adding weights
# Format: 'Label': (start, end, weight, row_index)
intervals = {
    "A1": (0.0, 3.0, 3, 3),
    "A2": (4.5, 8.0, 3, 3),
    "A3": (9.3, 11.5, 2, 3),
    
    "B1": (0.0, 5.2, 5, 2),
    "B2": (7.3, 10.2, 3, 2),
    
    "C1": (1.0, 3.6, 2, 1),
    "C2": (4.5, 8.2, 4, 1)
}

# 2. Build the Weighted Conflict Graph
G_weighted = nx.Graph()

# Add nodes with their respective weights
for node, data in intervals.items():
    G_weighted.add_node(node, weight=data[2])

# Add an edge if two intervals overlap
keys = list(intervals.keys())
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        u, v = keys[i], keys[j]
        start_u, end_u, weight_u, _ = intervals[u]
        start_v, end_v, weight_v, _ = intervals[v]
        
        # Intersection logic: Max of starts < Min of ends
        if max(start_u, start_v) < min(end_u, end_v):
            G_weighted.add_edge(u, v)

# 3. Visualize the Graph Structure (Headless-safe generation)
labels = {node: f"{node}\n(w={data[2]})" for node, data in intervals.items()}
pos = {node: ((data[0] + data[1]) / 2, data[3]) for node, data in intervals.items()}

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Weighted Interval Scheduling encoded as Maximum Weight Independent Set\n(Edges show time conflicts)", fontsize=12, pad=20)

nx.draw_networkx_nodes(G_weighted, pos, node_size=1500, node_color='bisque', edgecolors='black', ax=ax)
nx.draw_networkx_labels(G_weighted, pos, labels=labels, font_size=9, font_weight='bold', ax=ax)
nx.draw_networkx_edges(G_weighted, pos, width=2.0, edge_color='indigo', alpha=0.6, ax=ax)

ax.axis('off')
fig.tight_layout()

# Save once using explicit figure handle
output_path = "independent_set_graph_C.png"
fig.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Graph successfully generated and saved to: {output_path}")

plt.close(fig)

# 4. Find Maximum Weight Independent Set (Brute force calculation for verification)
def find_mwis(graph):
    best_weight = 0
    best_set = []
    nodes = list(graph.nodes())
    
    for r in range(len(nodes) + 1):
        for subset in combinations(nodes, r):
            is_independent = True
            for u, v in combinations(subset, 2):
                if graph.has_edge(u, v):
                    is_independent = False
                    break
            if is_independent:
                current_weight = sum(graph.nodes[node]['weight'] for node in subset)
                if current_weight > best_weight:
                    best_weight = current_weight
                    best_set = subset
    return best_set, best_weight

mwis_set, mwis_weight = find_mwis(G_weighted)
print(f"Optimal Schedule (Maximum Weight Independent Set): {sorted(list(mwis_set))}")
print(f"Maximum possible total weight (profit): {mwis_weight}")