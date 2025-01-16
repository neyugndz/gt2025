import heapq

# Function to create weighted adjacency matric
def create_weighted_adjacency_matrix():
    size = 9 
    adj_matrix = [[0] * size for _ in range(size)]
    
    # List of  predefined edges following this format (u, v, w)
    # u and v are nodes while w are weight of the edge
    edges = [
        (1, 2, 4), (1, 5, 1), (1, 7, 2),
        (2, 3, 7), (2, 6, 5),
        (3, 4, 1), (3, 6, 8),
        (4, 6, 6), (4, 7, 4), (4, 8, 3),
        (5, 6, 9), (5, 7, 10),
        (6, 9, 2),
        (7, 9, 8),
        (8, 9, 1),
        (9, 8, 7)
    ]
    
    # Element at position (i, j) represents the weight of the edge between nodes i+1 and j+1 
    for u, v, w in edges:
        adj_matrix[u-1][v-1] = w
        adj_matrix[v-1][u-1] = w
    return adj_matrix

def prim(adj_matrix, root):
    n = len(adj_matrix)
    
    # Visited list to track which nodes are included in the MST
    visited = [False] * n
    
    # Min-heap to store edges in the format (weight, from_node, to_node)
    min_heap = [(0, root, root)]
    mst_edges = []
    total_weight = 0
    
    # Process the heap until all nodes are visited or the heap is empty
    while min_heap:
        # Extract the edge with the minimum weight
        weight, from_node, to_node = heapq.heappop(min_heap)

        if visited[to_node]:
            continue
        
        # Mark the destination node as visited
        visited[to_node] = True
        
        # If it's not a dummy edge (from_node != to_node), add it to the MST
        if from_node != to_node:
            mst_edges.append((from_node + 1, to_node + 1, weight))  # Convert to 1-based index
            total_weight += weight  # Add edge weight to the total
        
        # Add all unvisited neighbors of the current node to the heap
        for neighbor in range(n):
            # Check if there is an edge and the neighbor is unvisited
            if adj_matrix[to_node][neighbor] != 0 and not visited[neighbor]:
                heapq.heappush(min_heap, (adj_matrix[to_node][neighbor], to_node, neighbor))
                
    return mst_edges, total_weight

def kruskal(adj_matrix):
    # List to store all edges in the graph in the format (weight, from_node, to_node)
    edges = []

    n = len(adj_matrix)
    
    # Extract all edges from the adjacency matrix
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] != 0:
                edges.append((adj_matrix[i][j], i, j))  # Store weight and node indices (0-based)
                
    edges.sort()
    
    # Disjoint Set Union (DSU) structures for Kruskal's algorithm
    # `parent` tracks the parent node for each node
    parent = list(range(n))
    
    # `rank` tracks the depth of trees to optimize union operations
    rank = [0] * n
    
    # Helper function to find the root (representative) of a node
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    # Helper function to union two sets (connect two components)
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        
        # If the roots are different, unite them
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                # If ranks are equal, arbitrarily attach one tree under the other
                parent[root_y] = root_x
                rank[root_x] += 1  # Increase the rank of the resulting tree
    
    mst_edges = []
    total_weight = 0
    
    # Iterate through all edges in sorted order
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)  # Merge the components of the two nodes
            mst_edges.append((u + 1, v + 1, weight))  # Convert to 1-based index
            total_weight += weight  # Add edge weight to the total

    return mst_edges, total_weight



adj_matrix = create_weighted_adjacency_matrix()
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)
    
root_node = int(input("\nEnter the root node for Prim's algorithm (1-9): ")) - 1

# Prim's Algorithm
prim_mst, prim_weight = prim(adj_matrix, root_node)
print("\nFor Prim's Algorithm, there is minimum spanning tree:")
for edge in prim_mst:
    print(f"Edge {edge[0]}-{edge[1]} with weight {edge[2]}")
print(f"Total Weight of MST (Prim's): {prim_weight}")

# Kruskal's Algorithm
kruskal_mst, kruskal_weight = kruskal(adj_matrix)
print("\nFor Kruskal's Algorithm, there is minimum spanning tree:")
for edge in kruskal_mst:
    print(f"Edge {edge[0]}-{edge[1]} with weight {edge[2]}")
print(f"Total Weight of MST (Kruskal's): {kruskal_weight}")