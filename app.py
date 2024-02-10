
from flask import Flask, json, request

app = Flask(__name__)

# Define a simple graph with distances between nodes
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 2, 'D': 6},
    'C': {'A': 10, 'B': 2, 'D': 4},
    'D': {'B': 6, 'C': 4}
}

# Define route for booking a cab
@app.route('/api/book_cab', methods=['GET'])
def book_cab():
    source = request.args.get('source')
    destination = request.args.get('destination')

    # Implement algorithm to find shortest path and calculate estimated cost
    shortest_time, estimated_cost = calculate_shortest_path(source, destination)

    return json({'shortestTime': shortest_time, 'estimatedCost': estimated_cost})

# Implement the algorithm to calculate shortest path and estimated cost
def calculate_shortest_path(source, destination):
    # Initialize distances with infinity
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0

    # Initialize predecessors
    predecessors = {}

    # List of nodes to be visited
    nodes = list(graph.keys())

    while nodes:
        # Find the node with the smallest distance value
        current_node = min(nodes, key=lambda node: distances[node])

        # Remove current node from list of unvisited nodes
        nodes.remove(current_node)

        # Update distances and predecessors for neighboring nodes
        for neighbor, weight in graph[current_node].items():
            potential_distance = distances[current_node] + weight
            if potential_distance < distances[neighbor]:
                distances[neighbor] = potential_distance
                predecessors[neighbor] = current_node

    # Backtrack to find the shortest path
    path = []
    while destination:
        path.insert(0, destination)
        destination = predecessors.get(destination, None)

    # Calculate estimated cost based on time and cab pricing
    total_time = distances[path[0]]
    cab_pricing = 0.5  # Placeholder value for cab pricing per minute
    estimated_cost = total_time * cab_pricing

    return total_time, estimated_cost

if __name__ == '__main__':
    app.run(debug=True)
