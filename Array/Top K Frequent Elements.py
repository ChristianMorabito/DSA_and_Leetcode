def top_k(nums, k):
	count = {}
	freq = [[] for _ in range(len(nums) + 1)]
	for n in nums:
		count[n] = 1 + count.get(n, 0)
	for n, c in count.items():
		freq[c].append(n)

	res = []

	for array in reversed(freq):
		if len(array) > 0:
			for num in array:
				res.append(num)
				if len(res) == k:
					return res


print(top_k([1, 1, 1, 2, 2, 2, 100], 3))
