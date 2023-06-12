# Encode & Decode algorithms - O(n) for both

# (1) Encode Function - input -> list_str = ['meow', 'says', 'the', 'cat']
#                       output -> '4#meow4#says3#the3#cat'
# l = str(len(s))                  ^^    ^^    ^^   ^^
# h = '#'                          lh    lh    lh   lh
def encode(list_str: list[str]) -> str:
    result = ""
    for s in list_str:
        result += str(len(s)) + "#" + s
    return result


# (2) Decode Function
# This function requires a main 'while loop' (i) (to go through the input 'encoded' string)
# & a brief nested 'while loop' (j), to venture out & find the delimiting '#' character.
# eg.       '4#meow4#says3#the3#cat'
# i = j      i ->  i ->  i -> i ->
#            j ->  j ->  j -> j ->
# The need for the nested 'while loop' (j) is because the number before the delimiting character (eg. 3#), could be
# more than one digit (eg. 11#), so there needs to first be a brief loop to iterate past the numbers to first get to
# the delimiter.
def decode(code: str) -> list[str]:
    result = []  # result variable is where the decoded strings will go.
    i = 0  # i variable is used to traverse through the code string.

    # The main (i) 'while loop' is used to traverse through the string. In every iteration, 'i' will begin at a
    # str(int), eg.        '1#I2#am2#me'
    #                       i  i   i
    while i < len(code):
        # 1) in every iteration, 'j' catches up to where 'i' is. eg. 1st iteration: i=0, therefore j=0
        # 2nd iteration: i=5, therefore j=5, etc.
        
        j = i
        # 2) while 'i' is still (not moving), 'j' briefly leads out to find the '#' delimiter.
        # once the delimiter is found, this nested loop has served it's purpose in the 'i' 'while loop' iteration.
        
        while code[j] != "#":
            j += 1

        # 3) between code[i] & code[j] is the encoded 'word length' number, that's before the '#', eg. code = '2#me'
        #                                                                                                      ij
        length = int(code[i:j])
        
        # 4) using 'j' as the index which is 1 before the encoded word & the word length number, the encoded word
        # can be found, & appended to the result list.
        result.append(code[j + 1: j + length + 1])
        
        # 5) now, 'i' has to be updated ahead, for the next loop iteration to move ahead to the next encoded str(int).
        i = j + length + 1
        
    return result


the_code = encode(["meow", "says", "the", "cat"])
print(the_code)
original_list = decode(the_code)
print(original_list)

