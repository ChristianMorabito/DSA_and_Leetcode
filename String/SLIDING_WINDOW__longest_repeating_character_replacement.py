# SLIDING WINDOW PROBLEM: O(n)
# Given a str of upper-case letters & int 'k', return the len of the longest sub-string containing the same letter.
# You are able to replace a letter 'k' times.
# Eg.   string =    'AAABB'; k = 2
#       return 5    because the two 'B's can be changed to 'A's, 'k' times.

# Strategy: because the goal is to return the len of the longest sub-string of same letter, then that
# substring can be within & including a sliding window. The right pointer will always increment forward within the
# loop, but the left pointer will only ever increment forward (shortening the window) when a condition is met.
# That condition is if ('window len' - 'most frequent letter within the window') is > than k
# Eg.   'AAABBB'; k = 2;    condition is False, so L pointer needn't increment, because window_len is 5
#        L   R              & most freq letter 'A's value is 3. So, 5 - 3 is not > than 2. but next iteration,
#                           when R is incremented, then L will inc too, because 6 - 3 is > than 2

def longest_repeating_char_replacement(string: str, k: int) -> int:
	# window is within & including L & R points
	letter_counter = {}  # var to count amount of letters within the window, eg. {'A': 3, 'B': 2}
	left = 0  # left pointer for sliding window
	max_freq = 0  # var to track which letter appears most within the window
	max_substring = 0  # var to track the widest window, aka max substring len

	for right in range(len(string)):  # right pointer for sliding window
		# below: dict 'get() method' is used to avoid a KeyError in the 1st instance the letter/char
		# is entered into the dict. value 0 is returned when the key does not exist.
		letter_counter[string[right]] = letter_counter.get(string[right], 0) + 1
		max_freq = max(max_freq, letter_counter[string[right]])

		# the below condition is entered when the window is too big to replace a letter k times.
		# the condition is True if: ('window len' - 'most frequent letter within the window') is > than k
		if (right - left) + 1 - max_freq > k:  # the + 1 is to account for indexing beginning at 0.
			# below: the value in dict[letter] at L pointer, is decremented
			# and the L pointer is moved across by one
			letter_counter[string[left]] -= 1
			left += 1

		# this is to update the max_substring value, if this has been the largest window/substring thus far
		# or if the previous sub_string was larger by 1
		max_substring = max(max_substring, (right - left) + 1)  # ((right - left) + 1) is the 'window/substring' len
	return max_substring


result = longest_repeating_char_replacement('ABAABBABB', 2)
# result = 5

