class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"NODE: [{self.value}]"


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


def cycle_detect(head) -> bool:
    # Floyd's Tortoise and Hare Algorithm
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


node = LinkedList()
# Fill LinkedList with nodes
node.append(0)
node.append(5)
node.append(10)
node.append(15)
node.append(20)
# Create cycle in linked list 0→ 5→ 10→ 15→ 20
node.cycle(10)  #                    ↖______↙

print(cycle_detect(node.head))
