import heapq



def dijkstra(graph, start):
    # Initialize distances dictionary
    distances = {vertex: float('infinity') for vertex in range(1, 23)}
    distances[start] = 0

    # Track previous vertices for path reconstruction
    previous = {vertex: None for vertex in range(1, 23)}

    # Priority queue for efficient minimum distance extraction
    # Format: (distance, vertex)
    priority_queue = [(0, start)]

    # Track processed vertices
    processed = set()

    while priority_queue:
        # Get vertex with minimum distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if already processed
        if current_vertex in processed:
            continue

        processed.add(current_vertex)

        # Process all neighbors
        for neighbor, weight in graph[current_vertex]:
            # Calculate potential new distance
            distance = current_distance + weight

            # Update if we found a better path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous


def reconstruct_path(previous, target):
    """Reconstruct the path from start to target vertex"""
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = previous[current]

    return path[::-1]  # Reverse to get path from start to target

