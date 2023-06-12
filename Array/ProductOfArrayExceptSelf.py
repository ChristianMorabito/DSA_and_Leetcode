# PRODUCT OF ARRAY EXCEPT SELF
# Example: array = [1, 2, 3, 4]  -->  result = [24, 12, 8, 6]
# Challenge: Avoid the divide operator.

def prod_without_self_WITHOUT(array):  # Without the divide operator. O(n)
    # 1) Create new array, with 1s, length of inputted array.
    res = [1] * len(array)  # res = [1, 1, 1, 1]
    prefix = 1
    for i in range(len(array)):
        res[i] = prefix
        prefix *= array[i]
    postfix = 1
    for i in range(len(array) - 1, -1, -1):
        res[i] *= postfix
        postfix *= array[i]
    return res  # This function returns a new array.


def prod_without_self_WITH_DIVIDE(array):  # With the divide operator. O(n)
    product = 1
    for i in range(len(array)):
        product *= array[i]  # 1) Create 'product', i.e. multiply all array number to each other.
    for i in range(len(array)):
        array[i] = product // array[i]  # 2) Divide product with each 'self' array number.
    # This function returns nothing but mutates original array..


prod_without_self_WITHOUT([1, 2, 3, 4])  # result = [24, 12, 8, 6]

#               -----Theory behind the first algorithm (avoiding divide operator)-----
#        STEP 1) CALCULATING THE PREFIX
# array =     1 [1, 2, 3, 4] 1 <-- imagine an invisible 1 being on the outside of the left & right of array.
#             |  |  |  |  |
# prefix =   [1, 1, 2, 6] 24   <-- because 24 is outside of list, it's ignored.

#        STEP 2) CALCULATING THE POSTFIX
# array =     1 [1, 2, 3, 4] 1
#                |  |  |  |  |
# postfix =     24[24,12, 4, 1]   <-- because 24 is outside of list, it's not used, so it will be 1.

#        STEP 3) CALCULATING BOTH (prefix[i] * postfix[i])
# prefix =  [1,  1,  2, 6]
# postfix = [24, 12, 4, 1]
# result =  [24, 12, 8, 6]

