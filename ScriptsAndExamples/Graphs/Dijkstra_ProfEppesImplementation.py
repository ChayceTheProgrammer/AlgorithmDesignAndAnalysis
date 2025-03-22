#using igraph to visualize effectively
import igraph as ig
import heapq


def create_escape_route_graph():
    """
    Creates a graph representing the road network based on the map.
    Vertices are waypoints 1-22, and edges represent direct road connections.
    Edge weights: 1 for green roads (desirable), 2 for orange roads (less desirable).
    """
    # Create empty graph with 22 vertices
    g = ig.Graph(n=22, directed=False)

    # Name the vertices
    g.vs["name"] = [str(i) for i in range(1, 23)]

    # Define edges with weights based on the map
    # Format: (source, target, weight)
    #indexing from zero so subtract one from mental index assumption
    edges_with_weights = [
        # Direct connections from waypoint 1
        (0, 1, 1),  # 1-2 (green)
        (0, 10, 1),  # 1-11 (green)

        # Connections from waypoint 2
        (1, 2, 1),  # 2-3 (green)

        # Connections from waypoint 3
        (2, 3, 1),  # 3-4 (green)

        # Connections from waypoint 4
        (3, 4, 1),  # 4-5 (green)

        # Connections from waypoint 5
        (4, 5, 2),  # 5-6 (orange)

        # Connections from waypoint 6
        (5, 6, 1),  # 6-7 (green)
        #considered (5, 6, 2) as yellow

        # Connections from waypoint 7
        (6, 7, 1),  # 7-8 (green)
        (6, 4, 1),  # 7-5 (green)

        # Connections from waypoint 8
        (7, 8, 2),  # 8-9 (yellow)

        # Connections from waypoint 9
        (8, 9, 2),  # 9-10 (orange)
        (8, 18, 1),  # 9-19 (green)

        # Connections from waypoint 10
        (9, 17, 2),  # 10-18 (orange)
        (9, 10, 1),  # 10-11 (green)

        # Connections from waypoint 11
        (10, 11, 2),  # 11-12 (orange)
        (10, 16, 1),    #11-17 (green)

        # Connections from waypoint 12
        (11, 12, 2),  # 12-13 (yellow)

        # Connections from waypoint 13
        (12, 13, 2),  # 13-14 (yellow)
        (12, 20, 1),  # 13-21 (green)

        # Connections from waypoint 14
        (13, 14, 1),  # 14-15 (green)
        (13, 19, 1),    #14-20 (green)
        (13, 15, 2),    #14-16 (yellow @ 16?)

        # Connections from waypoint 15
        #end node?
        #(14, 15, 1),  # 15-16 (green)

        # Connections from waypoint 16
        (15, 16, 1),  # 16-17 (green) [potentially yellow]
       #(15, 16, 2),

        # Connections from waypoint 17
        (16, 17, 2),  # 17-18 (yellow)

        # Connections from waypoint 18
        #end node (idk if 18-19 is connected but there is a spec of orange)
        (17, 18, 2),  # 18-19 (yellow)

        # Connections from waypoint 19
        #End node
        #(18, 21, 2)

        # Connections from waypoint 20
        (19, 20, 2),  # 20-21 (yellow)
        (19, 21, 1), #20-22 (green)

        # Connections from waypoint 21
        (20, 21, 2)  # 21-22 (some yellow)

    ]

    # Add edges to the graph
    # igraph uses 0-based indexing, but our waypoints are 1-based
    # so we've already adjusted the indices in edges_with_weights
    edges = [(e[0], e[1]) for e in edges_with_weights]
    weights = [e[2] for e in edges_with_weights]

    g.add_edges(edges)
    g.es["weight"] = weights

    return g


def dijkstra(graph, source, destinations):
    """
    Custom implementation of Dijkstra's algorithm using a priority queue

    Args:
        graph: igraph Graph object
        source: Index of source vertex
        destinations: List of destination vertex indices

    Returns:
        distances: Dictionary mapping vertex indices to distances from source
        previous: Dictionary for reconstructing shortest paths
    """
    n = graph.vcount()

    # Initialize distances with infinity for all vertices except source
    distances = {i: float('infinity') for i in range(n)}
    distances[source] = 0

    # Dictionary to store the previous vertex in the shortest path
    previous = {i: None for i in range(n)}

    # Priority queue for efficient minimum distance extraction
    # Format: (distance, vertex)
    priority_queue = [(0, source)]

    # Set to track processed vertices
    processed = set()

    # Track number of destinations found
    destinations_found = 0

    while priority_queue and destinations_found < len(destinations):
        # Get vertex with minimum distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if already processed
        if current_vertex in processed:
            continue

        # Mark as processed
        processed.add(current_vertex)

        # Check if this is a destination
        if current_vertex in destinations:
            destinations_found += 1

        # Process all adjacent vertices
        for edge in graph.incident(current_vertex):
            # Get the neighbor vertex
            neighbor = graph.es[edge].target if graph.es[edge].source == current_vertex else graph.es[edge].source

            # Skip if already processed
            if neighbor in processed:
                continue

            # Get edge weight
            weight = graph.es[edge]["weight"]

            # Calculate potential new distance
            distance = current_distance + weight

            # Update if we found a better path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous


def reconstruct_path(previous, start, target):
    """
    Reconstruct the path from start to target vertex

    Args:
        previous: Dictionary of previous vertices
        start: Starting vertex
        target: Target vertex

    Returns:
        List representing the path from start to target
    """
    path = []
    current = target

    while current is not None:
        # Add 1 to convert 0-based indices back to waypoint numbers
        path.append(current + 1)
        current = previous[current]

    # Reverse to get path from start to target
    return path[::-1]


def main():
    # Create graph based on the map
    g = create_escape_route_graph()

    # Define source (waypoint 1) and potential destinations
    source = 0  # 0-based index for waypoint 1
    destinations = [5, 7, 8, 14, 15, 21]  # 0-based indices for waypoints 6, 8, 9, 15, 16, 22

    # Run our custom Dijkstra's algorithm
    distances, previous = dijkstra(g, source, destinations)

    # Print distances to potential destinations
    print("Distances from waypoint 1 to potential destinations:")
    for dest in destinations:
        waypoint_num = dest + 1  # Convert to 1-based for display
        print(f"Waypoint {waypoint_num}: {distances[dest]}")

    # Find the destination with minimum distance (most likely escape route)
    min_distance = float('infinity')
    most_likely_destination = None

    for dest in destinations:
        if distances[dest] < min_distance:
            min_distance = distances[dest]
            most_likely_destination = dest

    # Convert back to 1-based waypoint number for display
    most_likely_waypoint = most_likely_destination + 1

    # Reconstruct and display the most likely escape route
    most_likely_path = reconstruct_path(previous, source, most_likely_destination)

    print(f"\nMost likely escape route: Waypoint {most_likely_waypoint}")
    print(f"Total distance (sum of weights): {min_distance}")
    print(f"Path: {' → '.join(map(str, most_likely_path))}")

    # Print all paths to potential destinations
    print("\nAll escape routes:")
    for dest in destinations:
        waypoint_num = dest + 1  # Convert to 1-based for display
        path = reconstruct_path(previous, source, dest)
        print(f"To waypoint {waypoint_num} (distance {distances[dest]}): {' → '.join(map(str, path))}")

    # Alternative: Use igraph's built-in shortest_paths function
    print("\nVerifying with igraph's built-in function:")
    for dest in destinations:
        waypoint_num = dest + 1  # Convert to 1-based for display
        path = g.get_shortest_paths(source, dest, weights='weight')[0]
        path_weights = [g.es[g.get_eid(path[i], path[i + 1])]["weight"] for i in range(len(path) - 1)]
        total_weight = sum(path_weights)
        # Convert 0-based indices to 1-based waypoint numbers
        path_waypoints = [p + 1 for p in path]
        print(f"To waypoint {waypoint_num} (distance {total_weight}): {' → '.join(map(str, path_waypoints))}")


if __name__ == "__main__":
    main()