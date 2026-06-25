import itertools
import matplotlib.pyplot as plt
import networkx as nx

# 1. Define the original bipartite edges from the image
bipartite_edges = [
    "L1-R1", "L1-R2",
    "L2-R1", "L2-R3",
    "L3-R2", "L3-R3", "L3-R4",
    "L4-R2", "L4-R4"
]

# 2. Build the Independent Set Graph (Line Graph)
G_is = nx.Graph()

# Each original edge becomes a vertex in the new graph
for edge in bipartite_edges:
    G_is.add_node(edge)

# Connect vertices if their original edges share an endpoint (conflict)
for edge1, edge2 in itertools.combinations(bipartite_edges, 2):
    l1, r1 = edge1.split('-')
    l2, r2 = edge2.split('-')
    
    # Conflict conditions: same left node OR same right node
    if l1 == l2 or r1 == r2:
        G_is.add_edge(edge1, edge2)

# 3. Visualize the Independent Set Problem (Headless-safe generation)
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title("Bipartite Matching Encoded as an Independent Set Problem\n(Vertices represent edges; Edges represent endpoint conflicts)", fontsize=12, pad=20)

# Circular layout makes it clean to see conflict cliques
pos = nx.circular_layout(G_is)

nx.draw_networkx_nodes(G_is, pos, node_size=1200, node_color='lightgreen', edgecolors='black', ax=ax)
nx.draw_networkx_labels(G_is, pos, font_size=9, font_weight='bold', ax=ax)
nx.draw_networkx_edges(G_is, pos, width=1.2, edge_color='tomato', alpha=0.7, ax=ax)

ax.axis('off')
fig.tight_layout()

# Save once using explicit figure handle
output_path = "independent_set_graph_B.png"
fig.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Graph successfully generated and saved to: {output_path}")

plt.close(fig)

# 4. Find Maximum Bipartite Matching via Independent Set
try:
    import networkx.algorithms.approximation as approx
    max_matching_set = approx.maximum_independent_set(G_is)
    print(f"Maximum Bipartite Matching found: {sorted(list(max_matching_set))}")
    print(f"Size of maximum matching: {len(max_matching_set)}")
except Exception as e:
    pass