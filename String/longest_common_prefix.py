def longest_common_prefix(string_list: list[str]) -> str:
	prefix = ""
	for i in range(len(string_list[0])):  # you only need to compare the first string with the rest
		for j in range(1, len(string_list)):
			if i == len(string_list[j]) or string_list[0][i] != string_list[j][i]:
				return prefix
		prefix += string_list[0][i]
	return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))



