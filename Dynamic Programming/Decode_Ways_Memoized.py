# Refer to Decode_Ways.png which shows recursive tree diagram
# to the exact string argument.

def decode_ways(string: str) -> int:

	cache = {}

	def dfs(i=0):

		# EARLY EXIT EDGE CASE - return 0
		if len(string) == 0:  # if string is empty, then return 0
			return 0

		# BASE CASE 1 - return 1                                         i  <-  string[i] == "0"
		# if i not at end of string, and it is on a "0", i.e. string = "1014", then return 0.
		# Although 0 is returned, marking it off as a 'dead end', what's beyond the string's "0",
		# i.e. "14", will be reached in the other recursive call (i+2), as the i steps over the "0".
		if i < len(string) and string[i] == "0":
			return 0

		# BASE CASE 2 - return 1
		# if i does not land on a string's "0", then it's reached a valid way.
		if i >= len(string)-1:
			return 1

		# MEMOIZATION - EARLY EXIT CACHE RETURN
		if i in cache:
			return cache[i]

		# (A) if        int(string[i] + string[i+1]) is < 10 or > 26, then single recursive call,
		# (B) else if   int(string[i] + string[i+1]) is >=10 or <=26, then double recursive calls.
		#
		# eg.    i  <- 64, so single path        i  <- 23, so forked path
		#   int("6411")                     int("2345")
#                ^^                              ^^
		# DOUBLE RECURSIVE PATHWAY (fib. seq.)
		curr = int(string[i] + string[i+1])
		if 10 <= curr <= 26:
			result = dfs(i+1) + dfs(i+2)  # fib sequence
			cache[i] = result
			return cache[i]

		# SINGLE RECURSIVE PATHWAY
		else:
			result = dfs(i+1)
			cache[i] = result
			return cache[i]

	return dfs()


print(decode_ways("6324120129"))

