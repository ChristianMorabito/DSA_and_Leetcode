def set_matrix_zeroes(array):
	ROWS, COLS = len(matrix), len(matrix[0])
	flag_row = False
	flag_col = False


	# Step 1)
	for i in range(ROWS):
		if matrix[i][0] == 0:
			flag_row = True

	# Step 2)
	for j in range(COLS):
		if matrix[0][j] == 0:
			flag_col = True

	# Step 3)
	for i in range(1, ROWS):
		for j in range(1, COLS):
			if matrix[i][j] == 0:
				# Set corresponding 0th col & corresponding 0th row to 0
				matrix[i][0] = matrix[0][j] = 0

	# Step 4)
	for i in range(1, ROWS):
		for j in range(1, COLS):
			if matrix[i][0] == 0 or matrix[0][j] == 0:
				matrix[i][j] = 0

	# Step 5)
	if flag_row:
		for i in range(ROWS):
			matrix[i][0] = 0

	# Step 6)
	if flag_col:
		for j in range(COLS):
			matrix[0][j] = 0

matrix = [
	[1, 0, 1],
	[1, 0, 1],
	[0, 1, 1]
]

set_matrix_zeroes(matrix)

for sub_array in matrix:
	print(sub_array)