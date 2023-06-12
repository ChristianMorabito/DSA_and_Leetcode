class Node:
    def __init__(self):
        self.children = {}
        self.end_word = False


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        cur = self.head
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end_word = True

    def search(self, word):

        def dfs(cur, j=0):
            # BASE CASE
            if j == len(word):
                return cur.end_word
            # SEARCH
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for key in cur.children:
                        # RECURSIVE SEARCH
                        if dfs(cur.children[key], i + 1):
                            return True
                if char not in cur.children:
                    return False
                cur = cur.children[char]
            return cur.end_word

        # CALL DFS FUNCTION
        return dfs(self.head)


trie = Trie()
trie.insert("carpet")
trie.insert("cary")
print(trie.search('car.'))


