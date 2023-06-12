# Two Pointer Technique      L                R
#                          [-2, 1, 3, 7, 14, 21]
def two_pointer_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        ans = nums[left] + nums[right]
        #                           L            <-- R
        if ans > target:        # [-2, 1, 3, 7, 14, 21]
            right -= 1
        #                           L -->            R
        elif ans < target:      # [-2, 1, 3, 7, 14, 21]
            left += 1
        else:
            return [left, right]


result = two_pointer_sum([-2, 1, 3, 7, 14, 21], 12)
print(result)  # [0, 4]
