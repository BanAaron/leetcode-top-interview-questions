from collections import defaultdict

graph_connections = defaultdict(list)
visited = set()

graph = {"0": ["1", "2"], "1": ["3", "4"], "2": ["5"], "3": [], "4": [], "5": []}


def visit(node):
    visited.add(node)


def dfs(node):
    # if we haven't seen this node yet
    if node not in visited:
        # we first store the node in our visited list
        visit(node)
        # then loop through the neighbours in the current node
        for neighbor in graph[node]:
            # recursively call dfs again. This will repeatedly loop through all possible nodes until there are none left
            dfs(neighbor)


if __name__ == "__main__":
    dfs("0")
