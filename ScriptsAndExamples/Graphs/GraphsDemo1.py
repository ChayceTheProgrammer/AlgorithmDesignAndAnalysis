# Simple graph implementation
class Graph:
    def __init__(self, weighted=False):
        self.adjacency_list = {}
        self.weighted = weighted

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2, weight=None):
        if self.weighted and weight is None:
            raise ValueError("Weight required for weighted graph")

        if node1 not in self.adjacency_list:
            self.add_node(node1)
        if node2 not in self.adjacency_list:
            self.add_node(node2)

        if self.weighted:
            self.adjacency_list[node1].append((node2, weight))
            self.adjacency_list[node2].append((node1, weight))  # For undirected graph
        else:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)  # For undirected graph

    def print_graph(self):
        for node, neighbors in self.adjacency_list.items():
            print(f"Node {node} connected to: {neighbors}")


# Example usage
# Unweighted graph
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.print_graph()

# Weighted graph
wg = Graph(weighted=True)
wg.add_edge('X', 'Y', 7)
wg.add_edge('X', 'Z', 9)
wg.add_edge('Y', 'Z', 5)
wg.print_graph()