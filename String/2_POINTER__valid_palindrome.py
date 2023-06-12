def is_palindrome_1(string):  # Solution ONE
    new = ""
    for i in string:
        if i.isalpha():
            new += i.lower()
    return new == new[::-1]


def is_palindrome_2(string):  # Solution TWO
    def alpha_num(char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))
    left = 0
    right = len(string) - 1
    while left < right:
        while left < right and not alpha_num(string[left]):
            left += 1
        while right > left and not alpha_num(string[right]):
            right -= 1
        if string[left].lower() != string[right].lower():
            return False
        left, right = left + 1, right - 1
    return True


print(is_palindrome_2("__________________________h.A/N*N   A|||H"))  # True. Because 'hannah' is palindrome

