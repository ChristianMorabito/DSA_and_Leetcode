def lic(array, i=0, prev=float("-inf"), cache=None) -> int:
	# BASE CASE
	if i == len(array):
		return 0

	# INITIALISE CACHE (ONLY IN 1ST FUNC CALL)
	if cache is None:
		cache = {}

	# CREATE KEY FOR CACHE DICT
	key = str(i) + " " + str(prev)

	# ACCESS RESULT IF AVAILABLE IN CACHE
	if key in cache:
		return cache[key]

	# RECURSIVE RELATION PT1 - first check if prev value in array is less than array[i].
	# if not, then LEAVE & move fwd.
	if array[i] <= prev:
		return lic(array, i+1, prev, cache)

	# RECURSIVE RELATION PT2 - if above condition was not met, then the prev array value is less than array[i],
	# so 1 can be added & array[i] becomes the new prev in the next func call.
	# the max func holds the TAKE/LEAVE func calls.
	result = max(1 + lic(array, i+1, array[i], cache), lic(array, i+1, prev, cache))

	# INSERT RESULT INTO CACHE
	cache[key] = result
	return cache[key]


print(lic([1, 2, 3, 1, 4]))

