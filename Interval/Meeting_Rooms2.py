class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def can_attend_meetings(intervals) -> int:  # [(0, 30)(5, 10)(10, 20)]
    start = sorted([i.start for i in intervals])  # start = [0, 5, 10]
    end = sorted([i.end for i in intervals])  # end = [10, 20, 30]
    result, count = 0, 0
    s, e = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
            result = max(result, count)
        else:
            e += 1
            count -= 1
    return result


meeting1 = Interval(0, 30)
meeting2 = Interval(5, 10)
meeting3 = Interval(10, 20)

print(can_attend_meetings([meeting1, meeting2, meeting3]))

