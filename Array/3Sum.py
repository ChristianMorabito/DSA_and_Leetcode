# Algorithm uses Two Pointer Technique. O(n^2)
# (1) 'for loop' moves 'i'
# (2) nested within that loop is a 'while loop' which moves the L & R pointers.
# (3) to find the right combination to equal target. answer = nums[i] + nums[L] + nums[R]
# (4) 'answer' value is compared with 'target' value.
#                   i  L ->      <- R
# eg. iteration 1: [1, 3, 5, 8, 18, 7]
#
#                      i  L ->   <- R
# eg. iteration 2: [1, 3, 5, 8, 18, 7]
def three_sum(nums, target):
    result = []  # Unique indexes of triplet which equals target are stored here.
    nums.sort()  # In order for the 'two pointer technique' to be used, the list much be sorted (ascending).
    # Ascended list looks like this: [-2, -1, 0, 0, 2, 3, 7, 8, 11, 11, 34, 35]
    for i in range(len(nums)):
        if nums[i] == nums[i-1]:  # this is to skip over same numbers. Eg. [0, 0, 2, 3] i=1 is skipped to i=2
            continue
        left, right = i+1, len(nums) - 1

        while left < right:
            answer = nums[i] + nums[left] + nums[right]
            if answer < target:
                left += 1
            elif answer > target:
                right -= 1
            else:
                result.append([i, left, right])
                left += 1  # After a triplet is found, it's unnecessary to move both L & R pointers.
                # Only moving one across is enough to find a unique triplet.
                while nums[left] == nums[left - 1] and left < right:
                    left += 1  # Similar to the 1st 'if' statement at the beginning,
                    # this is so the 'left' pointer can skip over a duplicate number.
                    # Another 'while' loop could be made for the right side, but this is redundant, because again,
                    # only moving one pointer across is enough to find a unique triplet.
    return result


indexes = three_sum([11, 0, 34, -2, -1, 11, 8, 7, 3, 0, 2, 35], 1)
# indexes [[0, 2, 5], [1, 2, 4]]
