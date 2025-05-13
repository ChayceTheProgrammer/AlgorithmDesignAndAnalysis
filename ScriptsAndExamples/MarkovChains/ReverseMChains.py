import numpy as np
from scipy.linalg import eig

# Define the forward transition matrix of the Markov chain
forward_transition_matrix = np.array([
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


# Compute the stationary distribution for the forward chain
stationary_distribution = compute_stationary_distribution(forward_transition_matrix)


# Function to compute the reverse transition matrix
def compute_reverse_transition_matrix(forward_matrix, stationary_distribution):
    """
    Computes the reverse transition matrix for a reversible Markov chain.
    """
    num_states = len(forward_matrix)
    reverse_matrix = np.zeros_like(forward_matrix)

    for i in range(num_states):
        for j in range(num_states):
            # Reverse transition probability formula: π(j) * P(j, i) / π(i)
            reverse_matrix[i, j] = (
                    stationary_distribution[j] * forward_matrix[j, i] / stationary_distribution[i]
            )

    return reverse_matrix


# Compute the reverse transition matrix
reverse_transition_matrix = compute_reverse_transition_matrix(forward_transition_matrix, stationary_distribution)

# Print the results
print("Forward Transition Matrix:")
print(forward_transition_matrix)

print("\nStationary Distribution:")
for state, prob in zip(states, stationary_distribution):
    print(f"{state}: {prob:.4f}")

print("\nReverse Transition Matrix:")
print(reverse_transition_matrix)


# Verify reversibility (Kolmogorov's criterion)
def verify_reversibility(forward_matrix, reverse_matrix, stationary_distribution):
    """
    Verifies if the Markov chain is reversible by checking Kolmogorov's criterion.
    """
    num_states = len(forward_matrix)
    for i in range(num_states):
        for j in range(num_states):
            forward_flow = stationary_distribution[i] * forward_matrix[i, j]
            reverse_flow = stationary_distribution[j] * reverse_matrix[j, i]
            if not np.isclose(forward_flow, reverse_flow):
                return False
    return True


is_reversible = verify_reversibility(forward_transition_matrix, reverse_transition_matrix, stationary_distribution)
print("\nIs the Markov chain reversible?", is_reversible)