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


def same_tree(root, sub):
    if not root and not sub:
        return True

    if root and sub and root.value == sub.value:
        return same_tree(root.left, sub.left) and same_tree(root.right, sub.right)
    return False


def sub_tree(root, sub):
    if not sub:
        return True
    if not root:
        return False
    if root.value == sub.value:
        return same_tree(root, sub)
    return sub_tree(root.left, sub) or sub_tree(root.right, sub)


# TREE
bst1 = BST()
bst1.insert(5)
bst1.insert(6)
bst1.insert(3)
bst1.insert(1)
bst1.insert(4)

# SUB-TREE
bst2 = BST()
bst2.insert(3)
bst2.insert(1)
bst2.insert(4)

print(sub_tree(bst1.head, bst2.head))
