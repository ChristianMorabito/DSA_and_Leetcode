# SLIDING WINDOW O(n)
# This algo works by incrementing 'right' var via 'for' loop. Add every string[right] letter into a set() var. 
# The length of the set is essentially the 'counter' to find the max length sub-string.
# The moment string[right] lands on a letter that's already in the set, then the max length sub-string was already
# reached within that sliding window.
# So a nested 'while' loop is entered (within the 'for' loop) where the left var needs to remove all string[left]
# letters from the set & then increment, until string[right] is no longer in the set. 

# (1) 'abcac'      | (2) 'abcac'      | (3) 'abcac'      | (4) 'abcac'      |
#      L           |      L           |         L        |         L        |
#      R           |         R        |         R        |          R       | return
# res= 1           |res= 3            |res= 1            |res= 2            | max_res = 3
# set={'a'}        |set={'a','b','c'} |set={'a'}         |set={'a','b'}     |

def longest_sub_string(string):
	letter_set = set()
	left = 0
	result = 0
	for right in range(len(string)):  # ->  R       the 'for' loop increments the 'right' var.
		while string[right] in letter_set:  # --> L the 'while' loop pauses the 'right' var & increments the 'left' var
			letter_set.remove(string[left])
			left += 1
		letter_set.add(string[right])
		result = max(result, len(letter_set))
	return result


print(longest_sub_string('abcddbacg'))

