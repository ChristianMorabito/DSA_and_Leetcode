# O(n)
# Notes are shown in attached image & gif

def container_most_water(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        local_area = min(height[left], height[right]) * (right - left)
        max_area = max(local_area, max_area)
        
        if height[left] == height[right]:
            left += 1
            right -= 1
        elif height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


result = container_most_water([1, 8, 2, 2, 5, 4, 2, 3, 7])
print(result)
