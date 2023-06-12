# Return the size of the largest component in the adjacency list.
# E.g. if the adjacency list creates this ->  1--2  4--5
# then the largest component is 4             \ /   |  |
#                                              3    6--7
#

def largest_component(graph):  # undirected graph
    visited = set()
    max_count = 0

    def dfs(curr):
        if curr in visited:
            return 0

        visited.add(curr)
        size = 1

        for item in graph[curr]:
            size += dfs(item)
        return size

    for node in graph:
        max_count = max(max_count, dfs(node))
    return max_count


adjacency_list = {0: [8, 1, 5],
                  1: [0],
                  5: [0, 8],
                  8: [0, 5],
                  2: [3, 4],
                  3: [2, 4],
                  4: [3, 2]}
result = largest_component(adjacency_list)
print(result)
