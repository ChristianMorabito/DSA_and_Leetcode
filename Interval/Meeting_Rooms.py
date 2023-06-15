class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def can_attend_meetings(intervals) -> bool:
    count = 0
    intervals.sort(key=lambda x: x.start)  # sort the list by the 0th item in each tuple
    for i in range(1, len(intervals)):
        i1 = intervals[i-1]
        i2 = intervals[i]
        if i1.end > i2.start:
            count += 1
    return True


meeting1 = Interval(0, 30)
meeting2 = Interval(5, 10)
meeting3 = Interval(15, 20)

result = can_attend_meetings([meeting1, meeting2, meeting3])
print(result)
