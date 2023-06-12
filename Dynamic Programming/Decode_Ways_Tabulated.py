# O(n) space; O(1) time.
# Refer to the recursive solution to understand the algorithm better
# This problem doesn't require you to decode anything. Only to return the amount of decoded ways as int.
# Input string of numbers represent letters, i.e. A = 1, B = 2 ... Y = 25, Z = 26
# If a number is 0 or > 26 then it's invalid.
# It's important to understand the problem first & how zeroes implicates the problem,
#   E.g. all these input strings would return zero:
#                  "10", "01", "130"
#   for input "130", "1 3 0" <- the "0" on its own is invalid because it's before 'A', and for
#   "1 30" <- the "30" is above 26, so it's also invalid, because it's past 'Z'.


def decode_ways(string: str) -> int:
    # EDGE CASE - return 0 if the 1st number in the string is 0
    # or if the string is empty.
    if int(string[0]) == 0 or len(string) == 0:
        return 0

    previous = 1
    before_prev = 1
    for i in range(1, len(string)):
        curr = 0

        # This conditional considers single digits, i.e. 1, 2 ... 8, 9.
        if int(string[i]) != 0:
            curr += previous

        # This conditional considers double digits, i.e. 10, 11 ... 25, 26.
        if 10 <= int(string[i-1] + string[i]) <= 26:
            curr += before_prev

        previous, before_prev = curr, previous

    return previous


print(decode_ways("6324120129"))

