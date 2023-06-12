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


# SAME TREE FUNCTION: DEPTH FIRST SEARCH (recursive)
def same_tree_dfs(root1, root2) -> bool:
    if not root1 and not root2:
        return True

    if root1 and root2 and root1.value == root2.value:
        return same_tree_dfs(root1.left, root2.left) and same_tree_dfs(root1.right, root2.right)
    return False


# SAME TREE FUNCTION: BREADTH FIRST SEARCH (iterative)
def same_tree_bfs(root1, root2) -> bool:
    queue = deque()  # using deque() function from collections module allows popping first items from list at O(1).

    # The algorithm begins by first appending to the queue[] a tuple of paired tree roots.
    # root1 is the root of the 1st binary tree, & root2 is the root of the 2nd binary tree.
    queue.append((root1, root2))

    # Both trees are laid out in a single queue of 'tuple pairs', e.g. queue = [(A1, B1), (A2, B2), ...]
    #
    #   TREE1             TREE2       queue = [(A1, B1), (A2, B2), (A_None, B_None)]
    #     A1               B1
    #   /    \           /    \
    #  A2     A_None   B2      B_None
    #
    # Within the loop, paired nodes are pushed at the end of the queue to fill the queue in a BFS order, and also
    # nodes in the front are popped off the queue to be validated. If paired nodes aren't identical, False is returned.
    # Oppositely, if paired nodes are pushed onto the queue[] & then popped off until the queue is empty, then both
    # trees have passed through the queue in pairs, ultimately proving them identical,
    # so the loop is ended, & True is returned.
    while queue:
        node1, node2 = queue.popleft()
        if not node1 and not node2:
            continue
            # if both nodes are None, then the end of a leaf is reached.
            # e.g.  A1          B1
            #      /  \        /  \
            #  None    A3  None    B3
            #
            # In above example, when None is reached, then it is stepped over (via 'continue' statement),
            # & subsequently, (A3, B3) nodes are part of the next iteration.
        if (not node1 or not node2) or (node1.value != node2.value):
            return False
            # False is returned if a nodes are not identical.
            # e.g.  A1          B1
            #      /  \        /  \
            #    B2    A3  None    B3
            #    ^           ^
            #    node1  !=   node2

        queue.extend([(node1.left, node2.left), (node1.right, node2.right)])
        #                                                    ________tuple1________     ________tuple2________
        # queue.extend() appends x2 tuples, i.e. queue[..., (node1.left, node2.left), (node1,right, node2.right)]
    return True


# TREE ONE
bst1 = BST()
bst1.insert(5)
bst1.insert(3)
bst1.insert(1)
bst1.insert(4)

# TREE TWO
bst2 = BST()
bst2.insert(5)
bst2.insert(3)
bst2.insert(1)
bst2.insert(4)


same_tree_dfs(bst1.head, bst2.head)
same_tree_bfs(bst1.head, bst2.head)
