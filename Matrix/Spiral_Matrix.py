def spiral_matrix(matrix):
	result = []
	left, right = 0, len(matrix[0])
	top, bottom = 0, len(matrix)

	while left < right and top < bottom:
		# get every i in the top row
		for i in range(left, right):
			result.append(matrix[top][i])
		top += 1
		# get every i in the right col
		for i in range(top, bottom):
			result.append(matrix[i][right-1])
		right -= 1

		if not (left < right and top < bottom):  # important condition for when array closes in on itself
			break

		# get every i in the bottom row
		for i in reversed(range(left, right)):
			result.append(matrix[bottom-1][i])
		bottom -= 1

		# get every i in the left col
		for i in reversed(range(top, bottom)):
			result.append(matrix[i][left])
		left += 1

	return result


print(spiral_matrix([
	['a', 'b', 'c', 'd'],
	['e', 'f', 'g', 'h'],
	['i', 'j', 'k', 'l']
]))
