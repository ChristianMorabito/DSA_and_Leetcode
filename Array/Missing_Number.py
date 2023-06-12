def missing_number(nums):
    result = len(nums)
    for i in range(len(nums)-1):
        result += i - nums[i]
    return result


missing_number([0, 9, 8, 3, 5, 4, 7, 1, 3, 2])  # missing_number = 6

