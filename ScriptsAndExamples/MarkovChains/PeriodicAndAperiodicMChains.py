from igraph import Graph, plot
import numpy as np

"""
Explanation of the Script:
Periodic Markov Chain:
The states are arranged in a cycle: State 1 -> State 2 -> State 3 -> State 1.
The transition matrix ensures that the chain has a period of 3 (i.e., it takes exactly 3 steps to return to the starting state).
This is visualized as a directed cycle graph.
Aperiodic Markov Chain:
The states have self-loops and transitions to multiple other states with non-zero probabilities.
The transition matrix ensures that the chain is aperiodic (i.e., it can return to the starting state at irregular intervals).
This is visualized as a graph with multiple edges and self-loops.
Simulation:
The simulate_markov_chain function simulates the movement of the Markov chain for a given number of steps.
It prints the transitions and the probabilities at each step, along with the final path.
Visualization:
The create_markov_chain function uses the igraph library to create and visualize the Markov chain as a directed graph.
The nodes represent the states, and the edges represent the transition probabilities.
"""

# Define a periodic Markov chain
periodic_states = ["State 1", "State 2", "State 3"]
periodic_transition_matrix = [
    [0, 1, 0],  # State 1 transitions to State 2
    [0, 0, 1],  # State 2 transitions to State 3
    [1, 0, 0],  # State 3 transitions back to State 1
]

# Define an aperiodic Markov chain
aperiodic_states = ["State A", "State B", "State C"]
aperiodic_transition_matrix = [
    [0.5, 0.5, 0],  # State A transitions to State A or State B
    [0.2, 0.5, 0.3],  # State B transitions to State A, State B, or State C
    [0.3, 0.3, 0.4],  # State C transitions to State A, State B, or State C
]

# Function to create and visualize a Markov chain graph
def create_markov_chain(states, transition_matrix, title):
    g = Graph(directed=True)
    g.add_vertices(states)

    # Add edges with weights (transition probabilities)
    for i, from_state in enumerate(states):
        for j, to_state in enumerate(states):
            if transition_matrix[i][j] > 0:
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
        "vertex_color": "lightblue",  # Color of the nodes
        "edge_curved": 0.2,  # Curvature of the edges
        "title": title,
    }
    plot(g, **visual_style)

# Simulate a Markov chain
def simulate_markov_chain(states, transition_matrix, steps, start_state):
    current_state = states.index(start_state)
    path = [start_state]
    print(f"Starting simulation from {start_state}.")

    for step in range(steps):
        # Choose the next state based on the transition probabilities
        next_state = np.random.choice(
            range(len(states)), p=transition_matrix[current_state]
        )
        print(f"Step {step + 1}: Moving from {states[current_state]} to {states[next_state]} (Probability: {transition_matrix[current_state][next_state]:.2f})")
        path.append(states[next_state])
        current_state = next_state

    print(f"Final path: {' -> '.join(path)}\n")

# Visualize and simulate the periodic Markov chain
print("Periodic Markov Chain:")
create_markov_chain(periodic_states, periodic_transition_matrix, "Periodic Markov Chain")
simulate_markov_chain(periodic_states, periodic_transition_matrix, steps=10, start_state="State 1")

# Visualize and simulate the aperiodic Markov chain
print("Aperiodic Markov Chain:")
create_markov_chain(aperiodic_states, aperiodic_transition_matrix, "Aperiodic Markov Chain")
simulate_markov_chain(aperiodic_states, aperiodic_transition_matrix, steps=10, start_state="State A")