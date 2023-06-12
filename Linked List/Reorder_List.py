class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"[Node: {self.value}]"


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print_list(self):
        if self.head:
            current = self.head
            while current:
                print(current, end=" -> ")
                current = current.next
            print('NULL')
        else:
            print("List is empty")

    def reorder_list(self):
        # __STEP 1__: find middle w/ slow & fast pointers
        #             slow pointer is named mid because it'll stop at mid point of the list
        #             & fast pointer is named tail, since it'll stop at end/tail node.
        mid = self.head
        tail = self.head
        while tail and tail.next:  # this loop condition is to ensure tail lands on the last node
            # for either an odd or even list.
            if tail.next.next:
                tail = tail.next.next
                mid = mid.next
            else:
                tail = tail.next
        #
        # Example of after while loop: 1 -> 2 -> 3 -> NULL
        #                                   ^    ^
        #                                 mid    tail
        #
        # __STEP 2__: reverse 2nd half
        curr = mid.next

        mid.next = None  # IMPORTANT - this is explained below
        prev = mid
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Having mid.next set to None is important because mid will become the last node,
        # once the algorithm is complete, the middle node becomes the last node, e.g.
        # Original: 1 -> 2 -> 3 -> NULL     After loop: 1 -> 2 <- 3
        #                                                     ? NULL
        # After algorithm is complete:
        # 1 -> 3 -> 2 -> NULL



        # __STEP 3__: merge 2 halves
        curr_left = self.head
        curr_right = tail
        while curr_left:
            # Step A) store the nodes in curr_left.next & curr_right.next into temp holder variables
            #         to hold them in memory; otherwise these nodes will be removed from memory when
            #         curr_left.next & curr_right.next is rerouted.
            hold_right_nxt = curr_right.next
            hold_left_nxt = curr_left.next

            # Step B) cut the links from curr_left.next & curr_right.next by
            #         rerouting them. I.e. in 1st iteration, node1 (curr_left) will point to
            #         last node (curr_right). Now what was the last node (curr_right) is now
            #         the new node2, and it will point to the original node2 (hold_left_nxt).
            curr_left.next = curr_right
            curr_right.next = hold_left_nxt

            # Step C) now update the
            curr_left = hold_left_nxt
            curr_right = hold_right_nxt


# Create linked list
node = LinkedList()
for i in range(3):
    node.append(i)

# PRINT LIST
node.print_list()  # [Node: 1] -> [Node: 2] -> [Node: 3] -> [Node: 4] -> [Node: 5] -> NULL
node.reorder_list()
# PRINT REORDERED LIST
node.print_list()  # [Node: 1] -> [Node: 5] -> [Node: 2] -> [Node: 4] -> [Node: 3] -> NULL

