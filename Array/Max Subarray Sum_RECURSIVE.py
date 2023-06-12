def maxCrossingSum(array, low, mid, high):
	#  Mid-left max value check
	sm = 0
	left_sum = -10000
	for i in range(mid, low - 1, -1):
		sm = sm + array[i]

		if sm > left_sum:
			left_sum = sm

	#  Mid-right max value check
	sm = 0
	right_sum = -1000
	for i in range(mid, high + 1):
		sm = sm + array[i]

		if sm > right_sum:
			right_sum = sm

	# Return the max - whether it be the mid-left, mid-right, or mid-whole.
	return max(left_sum + right_sum - array[mid], left_sum, right_sum)


def maxSubArraySum(array, low, high):
	if low > high:
		return -10000

	if low == high:
		return array[low]

	m = (low + high) // 2

	# Return the maximum of three parts of the array: left half, right half & the middle overlap (of the halves).
	return max(maxSubArraySum(array, low, m - 1),  # Recursively break list into left half
	           maxSubArraySum(array, m + 1, high),  # Recursively break list into right half
	           maxCrossingSum(array, low, m, high))  # Function to find max in overlapping elements.


main_array = [2, 3, 4, 5, 7]
max_sum = maxSubArraySum(main_array, 0, len(main_array) - 1)
print("Maximum contiguous sum is", max_sum)

