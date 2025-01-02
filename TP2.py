from collections import defaultdict, deque

graph = {
    1: [2, 4],
    2: [3, 6],
    3: [],
    4: [],
    5: [4, 9, 5],
    6: [3, 4],
    7: [3, 5, 6, 8],
    8: [3, 9],
    9: []
}

def create_adjacency_matrix(graph, n):
    matrix = [[0] * n for _ in range(n)]
    for src, neighbors in graph.items():
        for dest in neighbors:
            matrix[src - 1][dest - 1] = 1
    return matrix

def find_weakly_connected_components(graph, n):
    visited = set()
    components = 0

    undirected_graph = defaultdict(set)
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            undirected_graph[node].add(neighbor)
            undirected_graph[neighbor].add(node)
    
    def bfs(node):
        queue = deque([node])
        while queue:
            current = queue.popleft()
            for neighbor in undirected_graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    for node in range(1, n + 1):
        if node not in visited:
            components += 1
            visited.add(node)
            bfs(node)
    
    return components

def find_strongly_connected_components(graph, n):
    visited = set()
    finish_stack = []

    def dfs(node, graph, collect_stack):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, graph, collect_stack)
        if collect_stack:
            finish_stack.append(node)

    for node in range(1, n + 1):
        if node not in visited:
            dfs(node, graph, True)

    transposed_graph = defaultdict(list)
    for src, neighbors in graph.items():
        for dest in neighbors:
            transposed_graph[dest].append(src)

    visited.clear()
    components = 0

    def dfs_transposed(node):
        visited.add(node)
        for neighbor in transposed_graph[node]:
            if neighbor not in visited:
                dfs_transposed(neighbor)

    while finish_stack:
        node = finish_stack.pop()
        if node not in visited:
            components += 1
            dfs_transposed(node)
    
    return components


n = 9
adj_matrix = create_adjacency_matrix(graph, n)
weakly_connected_components = find_weakly_connected_components(graph, n)
strongly_connected_components = find_strongly_connected_components(graph, n)

print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

print("\nNumber of Weakly Connected Components:", weakly_connected_components)
print("Number of Strongly Connected Components:", strongly_connected_components)