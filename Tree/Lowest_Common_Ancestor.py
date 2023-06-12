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


def lowest_common_ancestor(root, p, q):
    current = root

    while current:
        # traverse down left-side of the tree
        if p < current.value and q < current.value:
            current = current.left
        # traverse down right-side of the tree
        elif p > current.value and q > current.value:
            current = current.right
        # lowest point reached
        else:
            return current

# TREE
bst = BST()
bst.insert(5)
bst.insert(6)
bst.insert(3)
bst.insert(1)
bst.insert(4)
print(lowest_common_ancestor(bst.head, 3, 6))

#           5
#         /   \
#        3     6
#       / \
#      1   4
