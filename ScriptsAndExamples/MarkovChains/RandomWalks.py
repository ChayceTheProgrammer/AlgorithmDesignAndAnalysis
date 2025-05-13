import numpy as np
from igraph import Graph, plot
import random

# Define the edges of an undirected graph
edges = [
    (0, 1),  # Node 0 is connected to Node 1
    (0, 2),  # Node 0 is connected to Node 2
    (1, 2),  # Node 1 is connected to Node 2
    (1, 3),  # Node 1 is connected to Node 3
    (2, 4),  # Node 2 is connected to Node 4
    (3, 4),  # Node 3 is connected to Node 4
    (3, 5),  # Node 3 is connected to Node 5
]

# Create an undirected graph
g = Graph(edges=edges, directed=False)
g.vs["name"] = [f"Node {i}" for i in range(len(g.vs))]

# Visualize the graph
layout = g.layout("fr")  # Fruchterman-Reingold layout for better visualization
visual_style = {
    "vertex_label": g.vs["name"],
    "layout": layout,
    "bbox": (400, 400),
    "margin": 50,
    "vertex_size": 30,
    "vertex_color": "lightblue",
}
plot(g, **visual_style)

# Function to perform a random walk on the graph
def random_walk(graph, start_node, steps):
    """
    Simulates a random walk on an undirected graph.

    Args:
        graph: The undirected graph (igraph.Graph).
        start_node: The starting node for the random walk (integer index).
        steps: The number of steps to take in the random walk.

    Returns:
        A list of nodes visited during the random walk.
    """
    current_node = start_node
    walk = [current_node]
    print(f"Starting random walk at {graph.vs[current_node]['name']}.")

    for step in range(steps):
        # Get the neighbors of the current node
        neighbors = graph.neighbors(current_node)
        # Randomly choose the next node from the neighbors
        next_node = random.choice(neighbors)
        walk.append(next_node)
        current_node = next_node
        print(f"Step {step + 1}: Moved to {graph.vs[current_node]['name']}.")

    return walk

# Perform a random walk on the graph
start_node = 0  # Start at Node 0
steps = 10  # Number of steps for the random walk
walk = random_walk(g, start_node, steps)

# Print the final walk
walk_labels = [g.vs[node]["name"] for node in walk]
print("\nRandom Walk Path:")
print(" -> ".join(walk_labels))