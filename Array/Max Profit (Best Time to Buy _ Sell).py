# SLIDING WINDOW problem. Use two pointers: left & right, to find the highest number.
# Highest number is found by: profit = array[right] - array[left]


def max_profit(array):
    left, right = 0, 1
    max_p = 0
    while right < len(array):
        if array[left] < array[right]:
            profit = array[right] - array[left]
            max_p = max(max_p, profit)  # This variable will update if new max is found.
        else:
            left = right
        right += 1
    return max_p


result = max_profit([4, 5, 1, 4, 5, 8, 3])
print(result)
