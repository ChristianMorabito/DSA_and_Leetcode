# The iterative method has better time & space complexity because once the kth lowest element is reached,
# the function ends. Whereas the recursive method still has to complete the entire in_order DFS.

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    def __repr__(self):
        return f"Node: {self.value}"


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

    def kth_smallest_recursive(self, k):

        in_order = []

        def dfs(curr):
            if curr is None:
                return
            dfs(curr.left)
            in_order.append(curr.value)
            dfs(curr.right)

        dfs(self.head)
        return in_order[k-1]

    def kth_smallest_iterative(self, k):
        n = 0
        stack = []
        curr = self.head

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            n += 1
            curr = stack.pop()
            if n == k:
                return curr.value
            curr = curr.right


# TREE ONE
bst = BST()
bst.insert(20)
bst.insert(8)
bst.insert(4)
bst.insert(12)
bst.insert(10)
bst.insert(14)
bst.insert(22)

print(bst.kth_smallest_iterative(5))
