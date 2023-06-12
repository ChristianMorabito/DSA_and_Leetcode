class Node:
    def __init__(self):
        self.leaf = {}
        self.end = False


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        curr = self.head
        for char in word:
            if char not in curr.leaf:
                curr.leaf[char] = Node()
            curr = curr.leaf[char]
        curr.end = True

    def search(self, word):
        curr = self.head
        for char in word:
            if char not in curr.leaf:
                return False
            curr = curr.leaf[char]
        return curr.end

    def starts_with(self, prefix):
        curr = self.head
        for char in prefix:
            if char not in curr.leaf:
                return False
            curr = curr.leaf[char]
        return True


trie = Trie()
