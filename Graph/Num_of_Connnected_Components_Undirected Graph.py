# Number of Connected Components in an Undirected Graph
# part 1) convert edges array to an adjacency list.
# part 2) use agency list to perform algorithm

def connected_components_count(graph):  # undirected graph
    visited = set()
    count = 0

    def dfs(curr):
        if curr in visited:
            return False

        visited.add(curr)

        for item in graph[curr]:
            dfs(item)
        return True

    for node in graph:
        if dfs(node):
            count += 1
    return count


def edges_to_adjacency_list(edges):
    graph = {}
    for array in edges:
        a = array[0]
        b = array[1]
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph


adjacency_list = edges_to_adjacency_list([[0, 1], [1, 2], [2, 3], [3, 4]])
result = connected_components_count(adjacency_list)
print(result)
