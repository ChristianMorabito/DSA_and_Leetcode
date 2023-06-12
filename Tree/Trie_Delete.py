class Node:
    def __init__(self):
        self.children = {}
        self.end_word = False


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        cur = self.head
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()  # if the letter is not present, then add it in
            cur = cur.children[char]  # iterate to the next node
        cur.end_word = True

    def search(self, word):
        cur = self.head
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.end_word

    def delete(self, word):
        node = self.head

        def rec(cur, i=0):
            # BASE CASE
            if i == len(word):
                cur.end_word = False
                # once base case reached, then end of the word has been reached.
                # So cur.end_word can be updated from True to False, since the end_word attribute
                # is a marker which signifies the end of a word, and the goal in this function is to
                # delete the word e.g. if the 'word to delete' were 'kit':  ↙ cur.end_word = True
                #                                          head = k → i → [t] → t → e → [n]
                #                                                          ↙ cur.end_word = False
                #                                          head = k → i → t → t → e → [n]

                return len(cur.children) == 0
                # if the 'word to delete' is a smaller word within a larger word, like the 'kit'/'kitten' example
                # above, then the cur.children dictionary will not be empty. If it's not empty, then False is returned.
                # if it is empty, then True is returned which means only then is it safe to start deleting nodes.
                # eg. if removing 'kit' from 'kitten':
                #                ↙ cur.children is {'t': Node()'}; so, len(cur.children) is not 0, so False is returned
                # head = k → i → t → t → e → [n]
                #

            next_del = rec(cur.children[word[i]], i+1)  # RECURSIVE CALL, returns bool
            # straight after the recursive call reaches its base cases & returns a bool, it goes to the previous
            # rec func on the call stack.
            # E.g. 1) head = p → i → [t]
            #                         ^ base case reached; end_word = True; and True is also returned
            #      2) head = p → i → t
            #                    ^ now in prev stack func which means next node ('t')
            #                      can be deleted since it returned True.

            if next_del:
                del cur.children[word[i]]
                # accessing the ahead char/node for deletion is done by .children attribute.
                # The .children attribute is a dictionary which holds the 'ahead char' as key & the 'ahead node' as
                # value, e.g. cur.children is {'t': Node()'}
                #                            key^   value^
                # That's why deleting a .children dict item, breaks a node link.
                # e.g. The below image is a lower-level abstraction of the data structure:
                #   head
                #       ↳ Node().children{'p': Node()}
                #                              ↘.children{'i': Node()}
                #                                              ↘.children{'t': Node()}
                #                                                              ↘.children{}
            # DELETE SPECIAL CASES TO CONSIDER
            # Below are 3 conditions that must ALL be True so that once the previous stack function is re-entered (after
            # below bool is returned), the above next_del variable will == True, thus allowing for next node deletion
            # if required.
            return next_del and (not cur.end_word) and len(cur.children) == 0
            #   1) -- next_del is True --
            #     next_del is True only if True was returned at the base case. And True is only returned at the
            #     base case if the last character in the 'word to delete' is also at the last node.
            #     Eg1. head = c → a → [r] <- if deleting the word 'car', then this will return True
            #     Eg2. head = c → a → [r] → p → e → [t] <- if deleting the word 'car', then this will return False
            #
            #   2) -- (not cur.end_word) is True --
            #      TIP: (not cur.end_word) is the same as (cur.end_word is False)
            #      if cur.end is False, then this means that it's safe to delete that node because its deletion
            #      won't interfere with another smaller word.
            #      Eg1. if deleting the word 'carpet':
            #      .    head = c → a → [r] → p → e → t
            #                                ↑___↑___↑__ (cur.end is False) == True statement
            #                                            for all 3 nodes which hold char's: 'p', 'e', & 't'
            #      BUT...
            #           head = c → a → [r]
            #                           ↑ (cur.end is False) == False statement for this node;
            #                             therefore, no more deletions can occur from here on in the function.
            #
            #   3) -- (len(cur.children) == 0) is True --
            #      if (len(cur.children) == 0) is False, then the char from the 'word to delete' is at an intersection.
            #      e.g. head = b → i → [b]          <- 'bib'
            #                         ↘  t → [e]    <- 'bite'
            #
            #      The below image is a lower-level abstraction of the above example:
            #      Notice how 'b' & 't' are held in the children dictionary.
            #                                                                                             ↗ .children{}
            #      head                                                                                  |
            #      ↘ Node().children{'b': Node()}                                       ↗ .children{'e': Node()}
            #                             ↘.children{'i': Node()}                      |
            #                                             ↘.children{'b': Node(), 't': Node()}
            #                                                             |
            #                                                              ↘.children{}
            #
            #      If the 'word to delete' is 'bite', then 't' & 'e' would successfully be deleted, but then
            #      the len(cur.children) != 0, because cur.children still holds {'b': Node()} in it.
            #
            #      head
            #      ↘ Node().children{'b': Node()}
            #                             ↘.children{'i': Node()}
            #                                             ↘.children{'b': Node()}
            #                                                             |
            #                                                              ↘.children{}
            #      Therefore, it returns False.
        rec(node)  # call to recursive function


trie = Trie()
trie.insert('cart')
trie.insert('carls')
res = trie.delete('car')
print(res)