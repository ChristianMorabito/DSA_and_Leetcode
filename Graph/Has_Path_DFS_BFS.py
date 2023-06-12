from collections import deque


def has_path_dfs(graph, src, dst):  # dfs recursive
	if src == dst:
		return True

	for item in graph[src]:
		if has_path_dfs(graph, item, dst):
			return True
	return False


def has_path_bfs(graph, src, dst):  # bfs iterative
	queue = deque(src)
	while queue:
		curr = queue.popleft()
		for item in graph[curr]:
			queue.append(item)
			if item == dst:
				return True
	return False



g = {'f': ['g', 'i'],
     'g': ['h', 'j'],
     'h': [],
     'i': ['k', 'g'],
     'j': ['i'],
     'k': []}

print(has_path_bfs(g, 'f', 'j'))
print(has_path_dfs(g, 'f', 'j'))


