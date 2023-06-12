# This 'binary search' challenge is really simple when it's broken down.

def find_target(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
# 1) if nums[mid] == target, then mission complete.
        if nums[mid] == target:
            return mid
        
        # LEFT SORTED
        # 2a) if left half is completely sorted, i.e. L <= M,
        # 2b) then check if target is within that sorted half.
        #           if so, then remove right half, i.e. high = mid - 1
        # 2c) If target isn't in this half, then remove this left half,
        #           i.e. low = mid + 1
        elif nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
    
        # RIGHT SORTED
        # 3a,b,c) the logic is identical to step 2, but for the right side.
        else:
            if nums[mid] > target >= nums[high]:
                low = mid + 1
            else:
                high = mid - 1


result = find_target([4, 5, 6, 9, 10, 11, 0, 1, 2, 3], 1)
print(result)

