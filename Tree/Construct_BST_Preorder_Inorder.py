# Construct Binary Tree from Preorder and Inorder Traversal

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BST:
    def __init__(self):
        self.head = self.build_tree([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])


    def build_tree(self, preorder, inorder):
        if not preorder or not inorder:
            return

        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.build_tree(preorder[1:mid+1], inorder[:mid])
        root.right = self.build_tree(preorder[mid+1:], inorder[mid+1:])
        return root


bst = BST()

