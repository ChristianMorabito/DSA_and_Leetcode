def majority_element(nums: list[int]) -> int:
	threshold = len(nums) // 2
	nums.sort()
	count = 1
	for i in range(1, len(nums)):
		if nums[i] == nums[i-1]:
			count += 1
			if count > threshold:
				return nums[i]
		else:
			count = 1
	return nums[0]  # assumes that the list had only 1 item in it


print(majority_element([2, 2, 1, 1, 1, 2, 2]))
