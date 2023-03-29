from collections import defaultdict

graph_connections = defaultdict(list)
visited = set()

graph = {"0": ["1", "2"], "1": ["3", "4"], "2": ["5"], "3": [], "4": [], "5": []}


def visit(node):
    visited.add(node)


def dfs(node):
    if node not in visited:
        print(node)
        visit(node)
        for neighbor in graph[node]:
            dfs(neighbor)


if __name__ == '__main__':
    dfs("0")
