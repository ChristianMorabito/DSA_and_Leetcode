# I can be placed before V and X
# X can be placed before L and C
# C can be placed before D and M
def roman_to_int(s: str) -> int:
	roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	result = 0
	for i in range(len(s)):
		if i+1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
			result -= roman_map[s[i]]
		else:
			result += roman_map[s[i]]
	return result


print(roman_to_int("MCMXCIV"))  # 1994

