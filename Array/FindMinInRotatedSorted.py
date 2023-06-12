#        L               M                H
# EG.1  [12, 0, 1, 2, 3, 4, 5, 6, 9, 10, 11] if M < H: H = M

#       L               M               H
# EG.2 [3, 4, 5, 6, 9, 10, 11, 0, 1, 2, 3] if M > H: L = M + 1

def find_min(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return low


result = find_min([12, 0, 1, 2, 3, 4, 5, 6, 9, 10, 11])
print(result)
