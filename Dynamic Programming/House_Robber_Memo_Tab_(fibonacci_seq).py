# Whenever you encounter a house i, you have two choices:
# CHOICE 1:
#   Steal from house i, but then you have to maximize the stolen value up to house i-2,
#   because house i-1 is no longer an option. In this option, you add vi to your running total.
# CHOICE 2:
#   Don’t steal from house i, in which case you’re free to maximize the stolen value up to house i-1,
#   since that house is an option. In this option, you add nothing to your running total.

# Memoised Solution: Time = O(n); Space = O(n) <- due to cache

def hr_rec(nums: list[int], i: int = 0, cache=None) -> int:
    if cache is None:
        cache = {}

    # BASE CASE
    if i >= len(nums):
        return 0

    # ACCESS CACHE DATA
    if i in cache:
        return cache[i]

    result = max(hr_rec(nums, i + 2, cache) + nums[i], hr_rec(nums, i + 1, cache))
    
    # INSERT CACHE DATA
    cache[i] = result
    return result


print(hr_rec([1, 2, 8, 9, 2, 3, 4, 1, 9, 2, 7]))


# Tabulated Solution: Time = O(n); Space = O(1)
def hr_tab(nums: list[int]) -> int:

    a = nums[0]  # f(i - 2)
    b = nums[1]  # f(i - 1)

    for i in range(2, len(nums)):
        a, b = b, max(b, a + nums[i])

    return b if len(nums) > 2 else max(a, b)


print(hr_tab([1, 3, 1, 4, 7]))
