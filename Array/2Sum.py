# The strategy is if you minus the target from the iterated value, you are creating a
# 'difference value'. Then check if the 'difference value' is a key in the dictionary. 


def two_sum_good(nums, target):  #  This is the GOOD iteration
    prev_map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return


def two_sum_bad(nums, target):  #  This is the BAD iteration
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return


two_sum_good([15, 7, 10, 11, ], 18))


