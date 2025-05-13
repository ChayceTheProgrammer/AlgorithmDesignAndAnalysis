import numpy as np


def page_rank(adjacency_matrix, alpha=0.85, max_iterations=100, tol=1e-6):
    """
    Computes the PageRank scores using the power iteration method.

    Parameters:
        adjacency_matrix (numpy.ndarray): The adjacency matrix of the graph.
        alpha (float): Damping factor (probability of following a link).
        max_iterations (int): Maximum number of iterations.
        tol (float): Convergence tolerance.

    Returns:
        numpy.ndarray: The PageRank scores for each node.
    """
    num_nodes = adjacency_matrix.shape[0]

    # Normalize the adjacency matrix to create the transition probability matrix
    transition_matrix = adjacency_matrix / adjacency_matrix.sum(axis=0)

    # Initialize the PageRank scores with a uniform distribution
    pagerank_scores = np.ones(num_nodes) / num_nodes

    # Power iteration method
    for iteration in range(max_iterations):
        new_pagerank_scores = (1 - alpha) / num_nodes + alpha * transition_matrix @ pagerank_scores

        # Check for convergence
        if np.linalg.norm(new_pagerank_scores - pagerank_scores, ord=1) < tol:
            break

        pagerank_scores = new_pagerank_scores

    return pagerank_scores


# Example: A small graph with 4 pages (A, B, C, D)
# Adjacency matrix representation of the graph
# Rows represent links from a page, columns represent links to a page
adjacency_matrix = np.array([
    [0, 1, 1, 0],  # Page A links to B and C
    [0, 0, 0, 1],  # Page B links to D
    [1, 1, 0, 1],  # Page C links to A, B, and D
    [0, 0, 1, 0],  # Page D links to C
])

# Compute the PageRank scores
pagerank_scores = page_rank(adjacency_matrix)

# Display the results
pages = ["A", "B", "C", "D"]
print("PageRank Scores:")
for page, score in zip(pages, pagerank_scores):
    print(f"{page}: {score:.4f}")