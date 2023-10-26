def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:

	last = (m+n)-1

	while m > 0 and n > 0:

		if nums1[m-1] > nums2[n-1]:
			nums1[last] = nums1[m-1]
			m -= 1
		else:
			nums1[last] = nums2[n-1]
			n -= 1
		last -= 1

	while n > 0:

		nums1[last] = nums2[n-1]
		n -= 1
		last -= 1


list1, list2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
merge(list1, 3, list2, 3)
print(list1)
