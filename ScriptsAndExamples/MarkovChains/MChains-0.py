from igraph import Graph, plot
import numpy as np

# Define the cities (nodes) and their transition probabilities
cities = ["City A", "City B", "City C"]
transition_matrix = [
    [0.1, 0.6, 0.3],  # Probabilities of moving from City A
    [0.4, 0.4, 0.2],  # Probabilities of moving from City B
    [0.3, 0.3, 0.4],  # Probabilities of moving from City C
]

# Create a directed graph to represent the Markov chain
g = Graph(directed=True)
g.add_vertices(cities)

# Add edges with weights (transition probabilities)
for i, from_city in enumerate(cities):
    for j, to_city in enumerate(cities):
        g.add_edge(from_city, to_city, weight=transition_matrix[i][j])

# Visualize the graph
layout = g.layout("circle")
visual_style = {
    "vertex_label": g.vs["name"],  # Label the vertices with city names
    "edge_label": [f"{w:.2f}" for w in g.es["weight"]],  # Label edges with probabilities
    "layout": layout,
    "bbox": (400, 400),  # Size of the plot
    "margin": 50,  # Margin around the plot
    "vertex_size": 40,  # Size of the nodes
    "vertex_color": "lightblue",  # Color of the nodes
    "edge_curved": 0.2,  # Curvature of the edges
}
plot(g, **visual_style)

# Simulate the hero's movement
def simulate_markov_chain(transition_matrix, cities, steps, start_city):
    current_city = cities.index(start_city)
    path = [start_city]

    for _ in range(steps):
        # Choose the next city based on the transition probabilities
        next_city = np.random.choice(
            range(len(cities)), p=transition_matrix[current_city]
        )
        path.append(cities[next_city])
        current_city = next_city

    return path

# Simulate the hero's journey
start_city = "City A"
steps = 10
journey = simulate_markov_chain(transition_matrix, cities, steps, start_city)

# Print the journey
print(f"The hero's journey: {' -> '.join(journey)}")