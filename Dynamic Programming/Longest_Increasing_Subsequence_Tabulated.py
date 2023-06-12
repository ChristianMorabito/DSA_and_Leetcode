def lis(nums: list[int]) -> int:
    if len(nums) < 2:
        return len(nums)
    dp = [0] * len(nums)
    max_len = 0
    for i in range(len(nums)):
        max_prev_len = 0
        for j in range(i):
            if nums[i] > nums[j]:
                max_prev_len = max(max_prev_len, dp[j])
        dp[i] = max_prev_len + 1
        max_len = max(max_len, dp[i])

    return max_len


print(lis([1, 3, 2, 4, 2]))
