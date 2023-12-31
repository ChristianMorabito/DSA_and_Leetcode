from collections import deque

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


def flip_dfs_rec(head):  # DFS (Recursive)
    if not head:
        return
    head.left, head.right = flip_dfs_rec(head.right), flip_dfs_rec(head.left)
    return head


def flip_bfs(head):  # BFS (Iterative)
    if not head:
        return

    queue = deque([head])
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        node.left, node.right = node.right, node.left
    return head


def flip_dfs_iter(head: Node):  # DFS (Iterative)
    stack = [head]
    while stack:
        curr = stack.pop()
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
        curr.right, curr.left = curr.left, curr.right


bst = BST()
bst.insert(2)
bst.insert(3)
bst.insert(1)
bst.insert(4)

# Invert Binary Tree
flip_dfs_rec(bst.head)  # DFS
flip_bfs(bst.head)  # BFS


