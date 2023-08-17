# The solution to this problem uses O(1) space complexity,
# which makes this solution unique.

def set_matrix_zeroes(array):

	ROWS, COLS = len(array), len(array[0])
	row_flag = False
	col_flag = False

	# Step 1)
	for i in range(ROWS):
		if array[i][0] == 0:
			row_flag = True

	# Step 2)
	for i in range(ROWS):
		if array[0][i] == 0:
			col_flag = True

	# Step 3)
	for i in range(1, ROWS):
		for j in range(1, COLS):
			if array[i][j] == 0:
				array[0][j] = array[i][0] = 0

	# Step 4)
	for i in range(1, ROWS):
		for j in range(1, COLS):
			if array[0][j] == 0 or array[i][0] == 0:
				array[i][j] = 0

	# Step 5)
	if row_flag:
		for i in range(ROWS):
			array[i][0] = 0

	# Step 6)
	if col_flag:
		for j in range(COLS):
			array[0][j] = 0


matrix = [
	[1, 0, 1],
	[1, 0, 1],
	[0, 1, 1]
]

set_matrix_zeroes(matrix)

for sub_array in matrix:
	print(sub_array)