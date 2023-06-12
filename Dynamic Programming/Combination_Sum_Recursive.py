# Refer to Combination_Sum_Recursive.png
# The recursive technique in this dfs stores data in a global array, as opposed to the base case returning anything.

def combination_sum(nums: list[int], target: int) -> list[int]:
    # 'result' array will hold the sub-arrays of combinations which equal the target
    # e.g. target = 2; result = [[1, 1], [2]]
    result = []

    def dfs(i, current, amount) -> None:
        if amount == target:
            result.append(current.copy())
            return

        if i == len(nums) or amount > target:
            return

        current.append(nums[i])  # 1) Append to current[]
        dfs(i, current, amount + nums[i])  # 2) Repeat step 1), traversing down left-side, until reach base case
        current.pop()  # 3) Once base case is reached, the previous node is visited, last 'current' int is popped.
        dfs(i+1, current, amount)  # Right tree branch is now traversed, incrementing i.

    dfs(i=0, current=[], amount=0)
    return result


combination_sum([1, 2, 3], 3)  # -> [[1, 1, 1], [1, 2], [3]]
