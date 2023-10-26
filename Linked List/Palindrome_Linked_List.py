class Node:
	def __init__(self, val=0, next_node=None):
		self.val = val
		self.next = next_node


def is_palindrome(head: Node):
	# find middle (with slow pointer)
	fast = slow = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	# reverse LL from mid-point
	prev, curr = None, slow
	while curr:
		curr_next = curr.next
		curr.next = prev
		prev = curr
		curr = curr_next
	# compare head from right
	left, right = head, prev
	while left and right:
		if left.val != right.val:
			return False
		left, right = left.next, right.next
	return True


node1 = Node(5)
node2 = Node(1)
node1.next = node2
node3 = Node(1)
node2.next = node3
node4 = Node(1)
node3.next = node4
node5 = Node(5)
node4.next = node5
# 1 -> 3 -> 3 -> 1
print(is_palindrome(node1))
