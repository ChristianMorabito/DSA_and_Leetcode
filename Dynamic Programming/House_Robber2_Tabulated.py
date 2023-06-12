# This problem is essentially House Robber, but with a slight difference.
# You have to call the house_robber function twice and find the max between
# the two. But for one func call, iterate from nums[start+1] to nums[end],
# and for the other, iterate from nums[start] to nums[end-1]
#         L        R
#         |        |        <- call_1 = house_robber(array, L, R)
# nums = [1, 3, 5, 7, 9]
#            |        |     <- call_2 = house_robber(array, L, R)
#            L        R
#
#   return max(call_1, call_2)

def house_robber2(nums: list[int]) -> int:

    # This below helper function is just the original House Robber problem.
    def helper(_nums, left, right) -> int:
        a = 0  # f(a - 2)
        b = 0  # f(b - 1)
        for i in range(left, right + 1):
            a, b = b, max(b, a + _nums[i])
        return b

    end = len(nums) - 1
    return max(helper(nums, 1, end), helper(nums, 0, end-1))
#   return max(       14       ,        10                )


#                 max = |---10---|
result = house_robber2([1, 3, 5, 7, 9])
#                    max = |___14___|
# result = 14
