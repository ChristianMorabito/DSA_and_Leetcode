def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort()

    result = 0
    prev_end = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prev_end:
            prev_end = end
        else:
            result += 1
            prev_end = min(end, prev_end)
    return result


print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))

