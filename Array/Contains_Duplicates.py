def contains_duplicate(nums):
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False


result = contains_duplicate([1, 2, 3])
print(result)