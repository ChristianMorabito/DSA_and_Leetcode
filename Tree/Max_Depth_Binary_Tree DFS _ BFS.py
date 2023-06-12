from collections import deque


class Node:
	def __init__(self):
		self.left = None
		self.right = None
		self.value = None


class BST:
	def __init__(self):
		self.head = None

	def insert(self, value):
		node = Node()
		node.value = value
		if self.head:
			current = self.head
			while True:
				if current.value == value:
					return
				if current.value > value:
					if current.left:
						current = current.left
					else:
						current.left = node
						return
				else:
					if current.right:
						current = current.right
					else:
						current.right = node
						return

		self.head = node

	def count_dfs(self):  # DEPTH FIRST SEARCH (recursive)
		def dfs(root):
			if root is None:
				return 0

			return 1 + max(dfs(root.left), dfs(root.right))

		return dfs(self.head)

	def count_bfs(self):  # BREADTH FIRST SEARCH (iterative)
		def bfs(root):
			if root is None:
				return 0
			# the deque function makes a doubly-linked list.
			# Essentially meaning that if you pop the first item off from the list, it'll be in
			# O(1) time instead of O(n).
			queue = deque([root])
			level = 0
			while queue:
				for _ in range(len(queue)):
					node = queue.popleft()
					if node.left:
						queue.append(node.left)
					if node.right:
						queue.append(node.right)
				level += 1

			return level

		return bfs(bst.head)


bst = BST()
bst.insert(5)
bst.insert(10)
bst.insert(2)
bst.insert(4)
print(bst.count_dfs())  # DFS - STACK
print(bst.count_bfs())  # BFS - QUEUE

# bst.head =    5
#              /   \
#             2     10
#            /\     /\
#           X  4   X  X
#              /\
#             X  X
#
