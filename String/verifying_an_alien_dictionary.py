def is_alien_sorted(words: list[str], order: str) -> bool:
    char_key = {char: i for i, char in enumerate(order)}
    for i in range(len(words) - 1):
        word_1, word_2 = words[i], words[i+1]
        for j in range(len(word_1)):
            if j == len(word_2):
                return False
            if word_1[j] != word_2[j]:
                if char_key[word_2[j]] < char_key[word_1[j]]:
                    return False
                break
    return True


print(is_alien_sorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))