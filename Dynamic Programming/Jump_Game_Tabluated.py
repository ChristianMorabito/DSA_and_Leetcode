def jump_game(nums: list[int]) -> int:
    max_jmp = nums[0]
    for i in range(1, len(nums)):
        if max_jmp == 0 and i < len(nums):
            return False
        max_jmp -= 1
        max_jmp = max(max_jmp, nums[i])
    return True


print(jump_game([1, 1, 1, 1, 0]))

