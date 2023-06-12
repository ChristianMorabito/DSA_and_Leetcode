class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"NODE: {self.value}"


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

    def cycle(self, k):
        if self.head:
            current = self.head
            kth_node = current
            while current.next:
                if current.value == k:
                    kth_node = current
                current = current.next
            current.next = kth_node

        else:
            print("List is empty!")


def merge(list1, list2):
    # Hold onto the nodes through a head node
    dummy_head = Node()
    # Traverse down the list through the tail node
    dummy_tail = dummy_head

    while list1 and list2:
        if list1.value < list2.value:
            dummy_tail.next = list1
            list1 = list1.next
        else:
            dummy_tail.next = list2
            list2 = list2.next
        dummy_tail = dummy_tail.next

    if list1 or list2:
        dummy_tail.next = list1 if list1 else list2

    return dummy_head.next


node1 = LinkedList()
node2 = LinkedList()
# LL: 1
node1.append(1)
node1.append(3)
# LL: 2
node2.append(2)
node2.append(4)

merge(node1.head, node2.head)
