def alien_order(adjacency_list) -> str:
    visit = {}
    result = []

    def is_cycle_check(char):  # this dfs ensures that if cycle is found, that it is bypassed.
        if char in visit:
            return visit[char]

        visit[char] = True
        for neighbour in adjacency_list[char]:
            if is_cycle_check(neighbour):
                return True
        visit[char] = False
        result.append(char)
        return False

    for c in adjacency_list:
        if is_cycle_check(c):
            return ""
    result.reverse()
    return "".join(result)


def create_list(word_list: list[str]):
    adjacency_list = {char: set() for word in word_list for char in word}

    for i in range(len(word_list) - 1):
        word_1, word_2 = word_list[i], word_list[i+1]
        min_len = min(len(word_1), len(word_2))

        # edge case, check if both words are identical at same length
        # e.g. 'cars' comes after 'car', but it doesn't give us new information
        # about alphabet hierarchy.
        if len(word_1) > len(word_2) and word_1[:min_len] == word_2[:min_len]:
            return ""
        for j in range(min_len):
            if word_1[j] != word_2[j]:
                adjacency_list[word_1[j]].add(word_2[j])
                break
    print(adjacency_list)
    return adjacency_list


#
alien_dictionary = ['aa', 'ab', 'ac', 'c', 'ca', 'cb', 'cc']
print(alien_order(create_list(alien_dictionary)))
