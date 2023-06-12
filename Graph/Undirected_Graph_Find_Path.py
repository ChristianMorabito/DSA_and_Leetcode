def find_paths_undirected(graph, start, end):  # dfs recursive
    visited = set()

    def dfs(curr):
        if curr == end:
            return True

        if curr in visited:
            return False

        visited.add(curr)

        for item in graph[curr]:
            if dfs(item):
                return True
        return False

    return dfs(start)


graph = {'i': ['j', 'k'],
         'j': ['i'],
         'k': ['i', 'm', 'l'],
         'm': ['k'],
         'l': ['k'],
         'o': ['n'],
         'n': ['o']}

find_paths_undirected(graph, 'j', 'm')  # True
