# Both, iterative & recursive functions are shown.
# The pattern is the fibonacci sequence.

def iterative_climbing_stairs(n: int) -> int:  # O(n)

    if n < 0:
        print('Incorrect input. ', end="")
        return -1

    if n < 3:
        return n

    one = 1
    two = 2

    for _ in range(3, n+1):  # 1 + 1 + 2 + 3 + 5 + 8 + 13:
	one, two = two, one + two

    return current


def recursive_climbing_stairs(n: int) -> int:  # O(2^n)
    if n < 0:
        print('Incorrect input. ', end="")
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return recursive_climbing_stairs(n-1) + recursive_climbing_stairs(n-2)


print(iterative_climbing_stairs(4))
print(recursive_climbing_stairs(4))
