from igraph import Graph, plot
import numpy as np

"""
Explanation of the Script:
Graph Representation:
The states are represented as nodes in a directed graph.
The edges represent the transition probabilities between states, ensuring that every state is reachable from every other state (directly or indirectly).
Visualization:
The graph is visualized using igraph, with nodes labeled by state names and edges labeled with transition probabilities.
Simulation:
The simulate_irreducibility function simulates the Markov chain starting from a given state.
It tracks the states visited during the simulation and checks if all states are reachable.
Irreducibility Check:
If all states are visited during the simulation, the Markov chain is irreducible.
The console output provides step-by-step details of the transitions and the final result of the irreducibility check.
"""

# Define the states (nodes) and their transition probabilities
states = ["State 1", "State 2", "State 3", "State 4"]
transition_matrix = [
    [0.2, 0.3, 0.3, 0.2],  # Probabilities of moving from State 1
    [0.1, 0.4, 0.4, 0.1],  # Probabilities of moving from State 2
    [0.3, 0.3, 0.2, 0.2],  # Probabilities of moving from State 3
    [0.25, 0.25, 0.25, 0.25],  # Probabilities of moving from State 4
]

# Create a directed graph to represent the Markov chain
g = Graph(directed=True)
g.add_vertices(states)

# Add edges with weights (transition probabilities)
for i, from_state in enumerate(states):
    for j, to_state in enumerate(states):
        g.add_edge(from_state, to_state, weight=transition_matrix[i][j])

# Visualize the graph
layout = g.layout("circle")
visual_style = {
    "vertex_label": g.vs["name"],  # Label the vertices with state names
    "edge_label": [f"{w:.2f}" for w in g.es["weight"]],  # Label edges with probabilities
    "layout": layout,
    "bbox": (400, 400),  # Size of the plot
    "margin": 50,  # Margin around the plot
    "vertex_size": 40,  # Size of the nodes
    "vertex_color": "lightgreen",  # Color of the nodes
    "edge_curved": 0.2,  # Curvature of the edges
}
plot(g, **visual_style)

# Check irreducibility by simulating the Markov chain
def simulate_irreducibility(transition_matrix, states, steps, start_state):
    current_state = states.index(start_state)
    visited_states = set([start_state])
    print(f"Starting simulation from {start_state}.")

    for step in range(steps):
        # Choose the next state based on the transition probabilities
        next_state = np.random.choice(
            range(len(states)), p=transition_matrix[current_state]
        )
        visited_states.add(states[next_state])
        print(f"Step {step + 1}: Moving from {states[current_state]} to {states[next_state]} (Probability: {transition_matrix[current_state][next_state]:.2f})")
        current_state = next_state

    # Check if all states were visited
    if len(visited_states) == len(states):
        print("The Markov chain is irreducible: All states are reachable.")
    else:
        print("The Markov chain is not irreducible: Some states are not reachable.")

# Simulate the Markov chain to check irreducibility
start_state = "State 1"
steps = 20
simulate_irreducibility(transition_matrix, states, steps, start_state)