# Group Anagrams O(n)
# The technique is having a dictionary key as a tuple. The tuple is a character frequency count from a to z.
# The value that's paired with the tuple is a list of all the words that fit into that frequency count.
#                  a  b  c  d ... x  y  z
# dict_results = {(1, 2, 0, 0 ... 0, 1, 0): ['baby', 'abby'], ...}
def group_anagrams(string_list):
    results = {}  # Initialise the dictionary
    for string in string_list:
        freq_list = [0] * 26  # freq_list = [0, 0, 0, ... 0] each index represents a letter, i.e.   a, b, c, ... z
        for char in string:  # the freq_list will reinitialise after every string_list 'for loop' iteration
            # the calculation: ord(char) - ord('a') means that 'a' == index 0 to 'z' == index 26
            freq_list[ord(char) - ord('a')] += 1  # each string char. will increment in the freq_list
        if tuple(freq_list) not in results:  # for freq_list to be a dictionary key, it must become a tuple.
            results[tuple(freq_list)] = [string]  # eg. {(1, 0, 0...): ['eat']
        else:
            results[tuple(freq_list)] += [string]  # eg. ['eat'] + ['ate'] = ['eat, 'ate']
            # eg. {(1, 0, 0...): ['eat', 'ate']
    return results.values()
    # if the values() method is not called, then the return will look like this:
    # {(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'], ... }


grouping = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# grouping = dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])

