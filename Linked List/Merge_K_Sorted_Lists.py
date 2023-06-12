# The K-way merge is really simple when you break it down
# it essentially is performing 2way merges on k ALREADY SORTED lists.
# Refer to k_way_merge.jpg for visualisation

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"NODE: {self.value}"


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
        else:
            self.head = new_node


def merge_two(list1, list2):
    dummy = Node()
    tail = dummy

    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

        if list1 or list2:
            tail.next = list1 if list1 else list2

    return dummy.next


def merge_k_sorted(lists):
    if not lists:
        return None

    while len(lists) > 1:
        for i in range(0, len(lists)-1, 2):
            lists[i] = merge_two(lists[i], lists[i+1])
        lists = [lists[j] for j in range(0, len(lists), 2)]

    return lists[0]


def print_list(node):
    while node:
        print(node.value, end=" ")
        node = node.next


node1 = LinkedList()
node2 = LinkedList()
node3 = LinkedList()
node4 = LinkedList()

# LL: 1
node4.insert(6)
node4.insert(7)
# LL: 2
node1.insert(1)
node1.insert(3)
#LL: 3
node2.insert(2)
node2.insert(4)
#LL: 4
node3.insert(0)
node3.insert(5)

result = merge_k_sorted([node1.head, node2.head, node3.head, node4.head])
print_list(result)




