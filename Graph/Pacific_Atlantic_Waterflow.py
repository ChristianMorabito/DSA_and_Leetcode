def pacific_atlantic(heights):
	ROWS, COLS = len(heights), len(heights[0])
	pacific, atlantic = set(), set()

	def dfs(r, c, visit, prev_height):
		if (r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prev_height:
			return
		visit.add((r, c))
		dfs(r + 1, c, visit, heights[r][c])
		dfs(r - 1, c, visit, heights[r][c])
		dfs(r, c + 1, visit, heights[r][c])
		dfs(r, c - 1, visit, heights[r][c])

	for col in range(COLS):
		dfs(0, col, pacific, heights[0][col])
		dfs(ROWS - 1, col, atlantic, heights[ROWS - 1][col])

	for row in range(ROWS):
		dfs(row, 0, pacific, heights[row][COLS - 1])
		dfs(row, COLS - 1, atlantic, heights[row][COLS - 1])

	result = [item for item in pacific if item in atlantic]
	return result


array = [
	[1, 2, 2, 3, 5],
	[3, 2, 3, 4, 4],
	[2, 4, 5, 3, 1],
	[6, 7, 1, 4, 5],
	[5, 1, 1, 2, 4]
]

print(pacific_atlantic(array))
