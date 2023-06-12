def max_sub_array(array):
	current_max_sum = array[0]
	final_max_sum = array[0]

	for num in array[1:]:
		# 1st) Check which is larger: on its own or added with the next item.
		current_max_sum = max(num, current_max_sum + num)
		# 2nd) Now check if this is the largest item thus far or not.
		final_max_sum = max(final_max_sum, current_max_sum)
	return final_max_sum


print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



