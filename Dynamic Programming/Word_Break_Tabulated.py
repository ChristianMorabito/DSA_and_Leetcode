# This YouTube vid explains the algorithm well:
# https://www.youtube.com/watch?v=tSbBuiO1rXI
# Also, refer to code notes below.

def word_break(string: str, word_list: list[str]) -> bool:
	dp = [True] + [False] * len(string)
	for i in range(1, len(string)+1):
		for part in word_list:
			# check if prev sub-prob is True (cached in dp[])
			# AND, check if the variable: part, fits in end
			# of sliced string, eg.'llo' ends with 'lo'
			if dp[i - len(part)] and string[:i].endswith(part):
				dp[i] = True
				break
	return dp[-1]


word_break('hello', ['hel', 'l', 'lo'])  # returns True
# i  =  0   1   2   3   4   5
# dp = [T,  F,  F,  T,  F,  T]
#       ""  h   h  [h   h   h
#               e   e   e   e
#                   l]  l   l
#                       l  [l
#                           o]

