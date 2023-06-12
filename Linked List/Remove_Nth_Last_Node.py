# Remove nth node from end of list
# EXAMPLE - remove 3RD node from end of list
# [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> [7] -> [8] -> [9] -> [10] -> NONE
#                                                   ^ remove so that: ...[7] -> [9] ->...
# Step 1) create a dummy node to act as head. Create 2 pointers - left & right.
#           [dummy] -> [1] -> [2] -> ...
#              ^        ^
#             left     right
#
# Step 2) while n > 0, traverse right variable. Each traversal, n -= 1.
#           Once loop ends, right variable will be on [4].
# Step 3) then while right != None, traverse right & left, like below:
#           [1] -> [2] -> [3] -> [4] -> [5] -> ...
#                >>left>>             >>right>>
#                          |_____________| <- this is the size of n
#
# Step 4) once right is None, then have left.next = left.next.next
#
#           ... [7] -> [8] -> [9] -> [10] -> NONE
#               left                         right
#
#
#           ... [7] --------> [9] -> [10] -> NONE
#               left                         right
#
# Step 5) finally, return dummy.next (so the first empty head node is ignored).

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"NODE: {self.value}"


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head:
            current = self.head
            while current:
                print(current.value, end=" -> ")
                current = current.next
            print("NONE")

    def append(self, value):
        new_node = Node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def remove_nth_from_end(self, n):
        dummy = Node().next = self.head
        left = dummy
        right = dummy.next

        while right and n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy


def print_list(head):
    if head:
        current = head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("NONE")


node = LinkedList()
# create nodes
for i in range(1, 11):
    node.append(i)


dum = node.remove_nth_from_end(1)
print_list(dum)