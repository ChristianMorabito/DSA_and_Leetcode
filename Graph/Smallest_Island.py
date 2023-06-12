def smallest_island(grid):
	column_len = len(grid)
	row_len = len(grid[0])
	visited = set()
	min_size = float("inf")

	def dfs(col, row):
		if col == column_len or col < 0 or row == row_len or row < 0:
			return 0
		if grid[col][row] == 'W' or (col, row) in visited:
			return 0

		visited.add((col, row))
		size = 1
		size += dfs(col + 1, row)
		size += dfs(col - 1, row)
		size += dfs(col, row + 1)
		size += dfs(col, row - 1)

		return size

	for c in range(column_len):
		for r in range(row_len):
			if grid[c][r] == 'L':
				if (c, r) not in visited:
					local_size = dfs(c, r)
					min_size = min(min_size, local_size)
	return min_size


island = [
			['W', 'L', 'W', 'W', 'W'],
			['W', 'L', 'W', 'W', 'W'],
			['W', 'W', 'W', 'L', 'W'],
			['L', 'W', 'W', 'L', 'L'],
			['L', 'L', 'W', 'W', 'W']
]

print(smallest_island(island))
