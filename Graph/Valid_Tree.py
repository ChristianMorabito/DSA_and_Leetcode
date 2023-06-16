def edge_to_list(edges):
    adj_list = {}
    for a, b in edges:
        if a not in adj_list:
            adj_list[a] = []
        if b not in adj_list:
            adj_list[b] = []
        adj_list[a].append(b)
        adj_list[b].append(a)
    return adj_list


def valid_tree_recursive(n, edges):
    adj_list = edge_to_list(edges)
    visited = set()

    def dfs(curr, prev):
        if curr in visited:
            return False  # means it's a loop, therefore, not valid tree
        visited.add(curr)
        for neighbor in adj_list[curr]:
            if neighbor == prev:
                continue
            if not dfs(neighbor, curr):
                return False
        return True

    return dfs(edges[0][0], -1) and n == len(visited) if edges else None



print(valid_tree_recursive(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
