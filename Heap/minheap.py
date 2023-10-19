class MinHeap:
	def __init__(self, array=None):
		self.array = []
		if type(array) is list:
			self.array = array.copy()
			for i in reversed(range(len(self.array))):
				self._siftdown(i)

	def _siftup(self, i):
		parent = (i - 1) // 2
		while i != 0 and self.array[i] < self.array[parent]:
			self.array[i], self.array[parent] = self.array[parent], self.array[i]
			i = parent
			parent = (i - 1) // 2

	def _siftdown(self, i):
		left = 2 * i + 1
		right = 2 * i + 2
		while (left < len(self.array) and self.array[i] > self.array[left]) or (right < len(self.array) and self.array[i] > self.array[right]):
			smallest = left if (right >= len(self.array) or self.array[left] < self.array[right]) else right
			self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
			i = smallest
			left = 2*i + 1
			right = 2*i + 2

	def insert(self, element):
		self.array.append(element)
		self._siftup(len(self.array) - 1)

	def get_min(self):
		return self.array[0] if len(self.array) > 0 else None

	def extract_min(self):
		if len(self.array) == 0:
			return None
		min_value = self.array[0]
		self.array[0], self.array[-1] = self.array[-1], self.array[0]
		self.array.pop()
		self._siftdown(0)
		return min_value

	def update_by_index(self, i, new):
		old = self.array[i]
		self.array[i] = new
		if new < old:
			self._siftup(i)
		else:
			self._siftdown(i)

	def update(self, old, new):
		if old in self.array:
			self.update_by_index(self.array.index(old), new)


def heapsort(array):
	heap = MinHeap(array)
	return [heap.extract_min() for _ in range(len(heap.array))]


print(heapsort([9, 11, 18, 13, 15, 14, 7, 8, 12, 10, 4, 6, 3]))


