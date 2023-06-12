# TWO POINTER technique - O(n^2)
# The technique here is to iterate through a string, and for each char, a nested loop will utilse two pointers:
# L & R, to traverse away from the char to check if the char is the centre of a palindrome. An important note is that
# the algorithm must account for palindromes with both even & odd lengths. For example:
# EVEN scenario:    'abccba'            | ODD scenario:   'level'
#                    <-LR->             |                  <-L
#                                       |                    R->
# For the EVEN scenario: L, R = i, i+1; | For the ODD scenario: L, R = i, i

def longest_pal_sub(string: str) -> str:
    start, end = 0, 0  # These variables are just the measuring sticks to find the max substring size.
    for i in range(len(string)):  # The first loop is to go through each character in the string.
        
        # EVEN PALINDROME CHECK
        even_left, even_right = find_sub_index(string, i, i+1)  # Func call to iterate the L & R pointers
        if (even_right - even_left) + 1 > end - start:  # Check if L & R created the widest opening, ie. (R - L) + 1.
            start, end = even_left, even_right  # If it is, then it's updated in the start/end variables.

        # ODD PALINDROME CHECK
        odd_left, odd_right = find_sub_index(string, i, i)
        if (odd_right - odd_left) + 1 > end - start:
            start, end = odd_left, odd_right

    return string[start:end + 1]  # Return the largest palindrome substring


def find_sub_index(string: str, left: int, right: int) -> tuple:
    # 2 conditions for the while loop to work:
    # 1st) The L & R pointers must be within the string
    # 2nd) string[L] & string[R] must equal the same character; otherwise it's not a palindrome.
    while left >= 0 and right < len(string)\
            and string[left] == string[right]:
        left -= 1
        right += 1
    # The reason why returning L+1 & R-1, is because in the final iteration, L & R will go one too far out-of-bounds. 
    # Eg. (1) L = 0     (2) L = -1      (3) Loop is now over but L should be at 0 not -1.
    return (left + 1), (right - 1)  # Return a tuple which will equal either oddL, oddR or evenL, evenR


print(longest_pal_sub('mamma'))

