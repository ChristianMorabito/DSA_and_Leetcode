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


    def is_valid(self):

        def validate(curr, left, right):
            if curr is None:
                return True

            if left > curr.value > right:
                return False

            return validate(curr.left, curr.value, right) and validate(curr.right, left, curr.value)

        return validate(self.head, float("-inf"), float("inf"))



bst = BST()
bst.insert(20)
bst.insert(22)
bst.insert(4)

print(bst.is_valid())

