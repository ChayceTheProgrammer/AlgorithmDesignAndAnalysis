import igraph as ig
import matplotlib.pyplot as plt

# Create an empty graph
g = ig.Graph()

# Add 6 vertices (automatically indexed from 0 to 5)
g.add_vertices(6)

# Name the vertices for better readability
g.vs["name"] = ["A", "B", "C", "D", "E", "F"]

# Add edges by referring to vertex indices
g.add_edges([(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

print("Graph summary:", g.summary())
print("Vertices:", g.vs["name"])
print("Edges:", g.get_edgelist())

###
# Create a weighted graph
wg = ig.Graph()
wg.add_vertices(4)
wg.vs["name"] = ["W", "X", "Y", "Z"]

# Add edges with weights
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
weights = [6, 9, 4, 8, 7]

wg.add_edges(edges)
# Add weight attribute to edges
wg.es["weight"] = weights

print("Weighted graph summary:", wg.summary())
print("Edge weights:", wg.es["weight"])

def plot_graph(graph, title, weighted=False):
    # Set visual attributes
    visual_style = {}
    visual_style["vertex_size"] = 40
    visual_style["vertex_label"] = graph.vs["name"]
    visual_style["vertex_color"] = "lightblue"
    visual_style["edge_width"] = 1.5

    # For weighted graphs, show the weights
    if weighted:
        visual_style["edge_label"] = graph.es["weight"]

    # Use a layout algorithm
    visual_style["layout"] = graph.layout("kk")  # Kamada-Kawai layout

    # Plot the graph
    fig, ax = plt.subplots(figsize=(8, 6))
    ig.plot(graph, target=ax, **visual_style)
    plt.title(title)
    plt.axis('off')
    plt.show()


# Visualize the unweighted graph
plot_graph(g, "Unweighted Graph")

# Visualize the weighted graph
plot_graph(wg, "Weighted Graph", weighted=True)

# Analyze the graph
print("Shortest path from A to F:", g.get_shortest_paths("A", "F", output="vpath")[0])
print("Degree of each vertex:", g.degree())
print("Graph diameter:", g.diameter())
print("Is the graph connected?", g.is_connected())

# For the weighted graph - shortest paths considering weights
print("\nShortest weighted path from W to Z:",
      wg.get_shortest_paths("W", "Z", weights=wg.es["weight"], output="vpath")[0])

"""
import pandas as pd

# Create sample edge data
edge_data = pd.DataFrame({
    'source': ['A', 'A', 'B', 'B', 'C'],
    'target': ['B', 'C', 'C', 'D', 'D'],
    'weight': [5, 8, 3, 6, 2]
})

# Create graph from DataFrame
g_from_df = ig.Graph.DataFrame(edge_data, directed=False)

print("Graph from DataFrame:", g_from_df.summary())
plot_graph(g_from_df, "Graph from DataFrame", weighted=True)
"""