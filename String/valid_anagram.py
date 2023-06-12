def valid_anagram(string1, string2):
	letter_counter = {}  # Initialise empty dictionary
	for letter in string1:
		if letter in letter_counter:
			letter_counter[letter] += 1  # increment each letter
		else:
			letter_counter[letter] = 1  # if letter not in dict, then add it.
	# letter_counter = {'a': 2, 't': 2}
	for j in string2:
		if j in letter_counter:
			letter_counter[j] -= 1  # decrement each letter.
			if letter_counter[j] == 0:
				del letter_counter[j]  # if letter key == 0, then delete it from dictionary.
		else:
			return False

	return True

print(valid_anagram('atta', 'tata'))
# True