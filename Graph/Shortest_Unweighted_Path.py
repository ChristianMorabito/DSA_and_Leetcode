from collections import deque


def bfs(graph, start, goal):
    steps = {start: 0}
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        if curr == goal:
            return steps[goal]
        for neighbour in graph[curr]:
            if neighbour not in steps:
                steps[neighbour] = steps[curr] + 1
                queue.append(neighbour)


adjacency_list = {'A': ['B', 'E', 'C'],
                  'B': ['E', 'D', 'A'],
                  'C': ['F', 'G'],
                  'D': ['B', 'E'],
                  'E': ['D', 'B', 'A'],
                  'F': ['C'],
                  'G': ['C']}

print(bfs(adjacency_list, 'D', 'C'))
