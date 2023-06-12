def word_search(board: list[list[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])

    def dfs(row, col, i):
        if i == len(word):
            return True

        if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] != word[i]:
            return False

        temp = board[row][col]
        board[row][col] = '#'
        result = dfs(row+1, col, i+1) or dfs(row-1, col, i+1) or dfs(row, col+1, i+1) or dfs(row, col-1, i+1)
        board[row][col] = temp
        return result


    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False





res = word_search([["A", "B", "C", "E"],
                   ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]], "ABCCEDFSA")
print(res)






