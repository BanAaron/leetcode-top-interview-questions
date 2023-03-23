from collections import defaultdict

graph_connections = defaultdict(list)
visited = set()

graph = {
    "0": ["1"],
    "1": ["3", "4"],
    "2": ["5"],
    "3": [],
    "4": [],
    "5": []
}


def dfs(start):
    if start not in visited:
        print(start)
        visited.add(start)
        for neighbor in graph[start]:
            dfs(neighbor)


dfs("0")
