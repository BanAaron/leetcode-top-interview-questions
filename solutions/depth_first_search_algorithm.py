from collections import defaultdict

graph_connections = defaultdict(list)
visited = set()

graph = {
    "0": ["1", '2'],
    "1": ["3", "4"],
    "2": ["5"],
    "3": [],
    "4": [],
    "5": []
}


def dfs(node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)


dfs("0")