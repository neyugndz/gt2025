graph = {
    1: [3, 2],
    2: [6, 5],
    3: [4],
    4: [8],
    5: [7],
    6: [],
    7: [],
    8: []
}

# Function to create an adjacency matrix from the graph
def create_adjacency_matrix(graph, n):
    matrix = [[0] * n for _ in range(n)]
    for src, neighbors in graph.items():
        for dest in neighbors:
            matrix[src - 1][dest - 1] = 1
    return matrix

# Function for inorder traversal of the tree
def inorder_traversal(tree, node):
    if node not in tree:
        return []
    
    left = inorder_traversal(tree, tree[node][0]) if len(tree[node]) > 0 else []
    right = inorder_traversal(tree, tree[node][1]) if len(tree[node]) > 1 else []
    
    return left + [node] + right

n = 8
adj_matrix = create_adjacency_matrix(graph, n)
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)
    

x = int(input("Enter the node label to print subtree in Inorder: "))
inorder_result = inorder_traversal(graph, x)
print(f"Inorder Traversal of subtree rooted at node {x}: {inorder_result}")
