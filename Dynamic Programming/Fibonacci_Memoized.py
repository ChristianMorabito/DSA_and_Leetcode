def fib_rec(n: int, cache = None) -> int:

    if n < 0: return -1  # Error catch
    if n == 0 or n == 1: return n  # Base case


    if cache is None: cache = {}  # cache var is initialised as dict only in first func call.

    # if n in cache, then the fib calc has been done before through the binary tree, so
    # the fib result is returned to prevent the binary tree calc going again
    if n in cache: return cache[n]

    result = fib_rec(n-1, cache) + fib_rec(n-2, cache)
    cache[n] = result

    return result


print(fib_rec(5))