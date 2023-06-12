# To improve time complexity, add a delete_word method to TrieNode & replace it with line 34

class TrieNode:
    def __init__(self):
        self.word = {}
        self.is_word = False

    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.word:
                curr.word[char] = TrieNode()
            curr = curr.word[char]
        curr.is_word = True

    def prune_word(self, word):
        cur = self
        node_child_key = []
        for char in word:
            node_child_key.append((cur, char))
            cur = cur.word[char]

        for parent_node, child_key in reversed(node_child_key):
            targetNode = parent_node.word[child_key]
            if len(targetNode.word) == 0:
                del parent_node.word[child_key]
            return


def find_words(board, words) -> list:
    root = TrieNode()
    for w in words:
        root.add_word(w)

    ROWS, COLS = len(board), len(board[0])
    result, visit = [], set()

    def dfs(row, col, node, word):
        if row < 0 or col < 0 or row == ROWS or col == COLS or board[row][col] not in node.word or (row, col) in visit:
            return

        visit.add((row, col))
        node = node.word[board[row][col]]
        word += board[row][col]
        if node.is_word:
            result.append(word)
            root.prune_word(word)

        dfs(row + 1, col, node, word)
        dfs(row - 1, col, node, word)
        dfs(row, col + 1, node, word)
        dfs(row, col - 1, node, word)
        visit.remove((row, col))

    for r in range(ROWS):
        for c in range(COLS):
            dfs(r, c, root, "")
    return result


find_words([["o", "a"],
            ["e", "t"]], ["oat"])

