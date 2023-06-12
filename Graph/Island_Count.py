def island_count(grid):
	column_len = len(grid)
	row_len = len(grid[0])
	visited = set()
	count = 0

	def dfs(col, row):
		if col == column_len or col < 0 or row == row_len or row < 0:
			return 0
		if grid[col][row] == 'W' or (col, row) in visited:
			return 0

		visited.add((col, row))
		dfs(col + 1, row)
		dfs(col - 1, row)
		dfs(col, row + 1)
		dfs(col, row - 1)

		return 1

	for c in range(column_len):
		for r in range(row_len):
			if grid[c][r] == 'L':
				if (c, r) not in visited:
					count += dfs(c, r)
	return count


g = [
	['W', 'L', 'W', 'W', 'W'],
	['W', 'L', 'W', 'W', 'W'],
	['W', 'W', 'W', 'L', 'W'],
	['L', 'W', 'W', 'L', 'L'],
	['L', 'L', 'W', 'W', 'W']
]

g2 = [
	['W', 'L', 'W', 'W', 'L', 'W'],
	['L', 'L', 'W', 'W', 'L', 'W'],
	['W', 'L', 'W', 'W', 'W', 'W'],
	['W', 'W', 'W', 'L', 'L', 'W'],
	['W', 'L', 'W', 'L', 'L', 'W'],
	['W', 'W', 'W', 'W', 'W', 'W']
]

print(island_count(g2))
