def fizzbuzz(n):
	result = []
	for i in range(1, n+1):
		curr = ""
		if i % 3 == 0:
			curr += "Fizz"
		if i % 5 == 0:
			curr += "Buzz"
		result.append(str(i) if not curr else curr)
	return result


print(fizzbuzz(15))
