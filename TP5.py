import sys
import heapq
import pandas as pd

## Implement Dijkstra's Algorithm

class Graph:
    def __init__(self, vertices, edges):
        """
        Initializes the graph with vertices and edges.
        Constructs an adjacency matrix for efficient lookup.
        """
        self.vertices = vertices
        self.vertex_index = {vertex: idx for idx, vertex in enumerate(vertices)}
        self.adj_matrix = self.create_adjacency_matrix(edges)

    def create_adjacency_matrix(self, edges):
        """Creates an adjacency matrix representation of the graph."""
        n = len(self.vertices)
        adj_matrix = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            adj_matrix[i][i] = 0  # Distance to itself is zero

        for (u, v), weight in edges.items():
            u_idx, v_idx = self.vertex_index[u], self.vertex_index[v]
            adj_matrix[u_idx][v_idx] = weight
            adj_matrix[v_idx][u_idx] = weight  # Since it's an undirected graph

        return adj_matrix

    def dijkstra(self, source, target):
        """Finds the shortest path using Dijkstra's Algorithm."""
        if source not in self.vertex_index or target not in self.vertex_index:
            return None, float('inf')

        n = len(self.vertices)
        dist = {vertex: float('inf') for vertex in self.vertices}
        prev = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        pq = [(0, source)]  # (distance, vertex)

        while pq:
            current_dist, current_vertex = heapq.heappop(pq)

            if current_vertex == target:
                break

            if current_dist > dist[current_vertex]:
                continue

            current_idx = self.vertex_index[current_vertex]

            for neighbor_idx in range(n):
                weight = self.adj_matrix[current_idx][neighbor_idx]
                if weight < float('inf'):  # Valid edge
                    neighbor = self.vertices[neighbor_idx]
                    distance = current_dist + weight

                    if distance < dist[neighbor]:
                        dist[neighbor] = distance
                        prev[neighbor] = current_vertex
                        heapq.heappush(pq, (distance, neighbor))

        # Reconstruct path
        path = []
        at = target
        while at:
            path.append(at)
            at = prev[at]
        path.reverse()

        return path, dist[target]


# Define graph data
vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "L", "M"]
edges = {
    ("A", "B"): 4, ("A", "C"): 1, ("B", "F"): 3, ("C", "D"): 8,
    ("C", "F"): 7, ("D", "H"): 5, ("E", "F"): 1, ("E", "H"): 2,
    ("E", "L"): 2, ("F", "H"): 1, ("H", "G"): 3, ("H", "M"): 7,
    ("H", "L"): 6, ("G", "M"): 4, ("G", "L"): 4, ("L", "M"): 1
}

# Create graph instance
graph = Graph(vertices, edges)

# Display adjacency matrix
matrix = pd.DataFrame(graph.adj_matrix, index=vertices, columns=vertices)
print("Adjacency Matrix:")
print(matrix)

print("\nVertices:", vertices)
source = input("Enter source vertex: ").strip().upper()
target = input("Enter target vertex: ").strip().upper()

# Run Dijkstra's algorithm
path, total_weight = graph.dijkstra(source, target)

# Display results
if not path or total_weight == float('inf'):
    print(f"No path found from {source} to {target}.")
else:
    print(f"Shortest path from {source} to {target}: {' -> '.join(path)}")
    print(f"Total weight: {total_weight}")