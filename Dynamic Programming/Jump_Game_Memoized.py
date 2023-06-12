# There are two index variables used in this algorithm: 'i' & 'index'

def jump_game(nums, cache=None, index=0) -> bool:

    # INITIALISE CACHE
    if cache is None:
        cache = {}

    # BASE CASE - stop recursion once the 'index variable' lands on final array index.
    if index == len(nums) - 1:
        return True

    # ACCESS CACHE to bypass function call
    if index in cache:
        return cache[index]

    # Function is cached as False by default. It will remain False if the loop is bypassed.
    # The 'for loop' is only bypassed if 'i in range(1, 1)' <- this means that 0 iterations are done.
    # 0 iterations are only done if nums[index] == 0.
    # Why 'i' begins at 1 instead of 0 is explained below.
    cache[index] = False
    for i in range(1, nums[index] + 1):
        # i must begin at 1, instead of 0, because in the recursion call, index is incremented by i, so if
        # i == 0, then the index + 0 means it'll never increment, ultimately being stuck in an infinite loop.
        if jump_game(nums, cache, index + i):
            # INSERTING CACHE DATA AS: True
            # or...
            cache[index] = True
            return cache[index]
    # INSERTING CACHE DATA AS: False
    return cache[index]  # <- cache[index] remains False if the algorithm reaches here


print(jump_game([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0]))
