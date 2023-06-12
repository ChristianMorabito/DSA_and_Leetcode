class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node: {self.value}"


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            return current

        self.head = new_node
        return self.head

    def reverse(self):
        curr, prev = self.head, None
        while curr:
            # STEP 1) Hold on the node that's inside curr.next by storing it inside variable 'nxt'
            #         because in the subsequent step, current.next will point to variable 'prev'.
            nxt = curr.next
            # STEP 2) curr.next will let go of the node & point to 'prev'.
            curr.next = prev
            # STEP 3) 'prev' will become the current node, so that it can be the previous node in the
            #          next iteration.
            prev = curr
            # STEP 4) the current node 'curr' is now updated to 'nxt' which was the original node ahead.
            curr = nxt


node = LinkedList()
node.insert(0)
node.insert(5)
node.insert(10)
node.reverse()

# head = Node:0 -> Node:5 -> Node:10
