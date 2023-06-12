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

    def level_order_traversal(self):
        queue = deque([self.head])
        result = []
        while queue:
            level = []

            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.value)
                    
            if level:
                result.append(level)

        return result





bst = BST()
bst.insert(3)
bst.insert(2)
bst.insert(1)
print(bst.level_order_traversal())
# output [[3], [2, 20], [1, 15, 25]]



