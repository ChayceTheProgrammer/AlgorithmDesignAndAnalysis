import numpy as np
from scipy.linalg import eig
from igraph import Graph, plot

# Define the transition matrix of the Markov chain
transition_matrix = np.array([
    [0.5, 0.3, 0.2],  # Probabilities of moving from State 1
    [0.2, 0.6, 0.2],  # Probabilities of moving from State 2
    [0.3, 0.3, 0.4],  # Probabilities of moving from State 3
])

# Define the states
states = ["State 1", "State 2", "State 3"]


# Function to compute the stationary distribution
def compute_stationary_distribution(transition_matrix):
    """
    Computes the stationary distribution of a Markov chain.
    """
    # Solve the eigenvalue problem: P.T * π = π
    eigenvalues, eigenvectors = eig(transition_matrix.T)

    # Find the eigenvector corresponding to eigenvalue 1
    stationary_vector = eigenvectors[:, np.isclose(eigenvalues, 1)]

    # Normalize the eigenvector to make it a probability distribution
    stationary_distribution = stationary_vector / np.sum(stationary_vector)
    return stationary_distribution.real.flatten()


# Compute the stationary distribution
stationary_distribution = compute_stationary_distribution(transition_matrix)

# Print the stationary distribution
print("Stationary Distribution:")
for state, prob in zip(states, stationary_distribution):
    print(f"{state}: {prob:.4f}")


# Visualize the Markov chain
def visualize_markov_chain(states, transition_matrix, title):
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


# Visualize the Markov chain
visualize_markov_chain(states, transition_matrix, "Markov Chain with Stationary Distribution")