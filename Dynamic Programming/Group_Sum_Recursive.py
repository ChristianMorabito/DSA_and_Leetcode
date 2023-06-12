# Refer to Group_Sum_Recursive.png
# group_sum: This is a classic DP backtracking problem.
# Given an array (nums: list[int]) & a target int, use recursion to see if the numbers in the array (whether it be
# one, some or all the numbers) can add to equal the target. if it can equal the target, then return True, otherwise
# return False.
# E.g.  nums = [1, 2];  target = 1  <- True
#       nums = [1, 2];  target = 2  <- True
#       nums = [1, 2];  target = 3  <- True
#       nums = [1, 2];  target = 4  <- False

# nums = [1, 2, 3];  target = 4

def group_sum(nums: list[int], target: int, i: int = 0) -> bool:
    if i >= len(nums):
        return target == 0

    subtract = group_sum(nums, target - nums[i], i+1)
    skip = group_sum(nums, target, i+1)

    return subtract or skip


print(group_sum([1, 2, 3], 4))