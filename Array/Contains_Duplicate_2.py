def contains_duplicate(nums, k):
	duplicate = {}
	for i, num in enumerate(nums):
		if num in duplicate and abs(duplicate[num] - i) <= k:
			return True

		duplicate[num] = i
	return False


print(contains_duplicate([1, 2, 3, 1, 2, 3], 2))
