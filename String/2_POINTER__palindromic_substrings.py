# Comments here are brief because this algorithm is very similar to 'Longest Palindromic Substring' (so refer to those
# comments for clarification).

# Just like 'Longest Palindromic Substring' problem, even-lengthened & odd-lengthened palindromes must be considered.
# So two counts have to be performed. E.g. EVEN:    'aaa'   |   ODD:    'aaa'
#                                                  <-LR->   |          <-L
#                                     left, right = i, i+1  |            R->     left, right = i, i

def pal_sub_strings(s: str) -> int:  # this func is to iterate ever each string char
    counter = 0
    for i in range(len(s)):
        even_left, even_right = i, i+1
        odd_left, odd_right = i, i
        counter += sub_str_counter(s, even_left, even_right)
        counter += sub_str_counter(s, odd_left, odd_right)
    return counter


# this func is to count each substring (every time L & R move, that's a new substring to count)
def sub_str_counter(string: str, left: int, right: int) -> int:
    counter = 0
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
        counter += 1
    return counter


print(pal_sub_strings('aaaa'))
