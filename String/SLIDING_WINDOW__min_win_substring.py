def min_win_substring(s: str, t: str) -> str:
    # 'Quick exit' case - eg. s = 'A'; t = 'AB'; therefore, t will never fit into s
    if len(t) > len(s):
        return ""

    static_map = {}
    # 1) Create a char frequency map for t string. Eg. t = 'BBC'; static_map = {'B': 2, 'C': 1}
    # This map will be STATIC & used to compare against a window map (which will be dynamic).
    for char in t:
        static_map[char] = 1 + static_map.get(char, 0)

    window = {}
    have, need = 0, len(t)
    left = 0
    result, result_len = [-1, -1], float("infinity")

    for right in range(len(s)):
        char = s[right]
        # 2) Similarly to step 1, a char frequency map is made, but for t string. This map is named window, because
        # only chars between L & R window will be counted. Once the L pointer moves away from a char, that char is
        # decremented from the window map. So unlike the static map, this is a DYNAMIC map which is updated.
        window[char] = 1 + window.get(char, 0)
        #                                                                                                    LR
        # 3) If R pointer is on a char & that char is also in static_map, eg. static_map = {'A':1};     s = 'BAC'
        # AND the values of both maps are less-than or equal to, then the 'have var' can be incremented. For eg.
        # static_map = {'A':2}; window_map = {'A':1} <- this means that we HAVE one of the chars required.
        if char in static_map and window[char] <= static_map[char]:
            have += 1

        # 4) This below loop is entered when the dynamic window/map contains all the chars within the static map.
        while have == need:
            # 4A) Within this window, the result & result_len var can be updated to check if this is the smallest
            # window thus far.
            if (right - left) + 1 < result_len:
                result = [left, right]
                result_len = (right - left) + 1
            # 4B) Before the left pointer is incremented, the left item from the window/map is decremented.
            window[s[left]] -= 1
            # If L pointer is on a char & that char is also in static map AND the char value in the window is now
            # LESS than the static map, then the HAVE value != NEED anymore, thus the loop will be broken out of.
            if s[left] in static_map and window[s[left]] < static_map[s[left]]:
                have -= 1  # This is the exit condition to break out of the while loop
            left += 1  # 4C) Then the left pointer is incremented.

    left, right = result
    return s[left:right+1] if result_len != float("infinity") else ""


print(min_win_substring('ADOBECODEBANC', 'ABC'))

