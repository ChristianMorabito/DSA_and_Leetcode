def unique_paths(m, n, cache=None):
    if m == 1 or n == 1:
        return 1

    key = str(m) + " " + str(n)

    if cache is None:
        cache = {}

    if key in cache:
        return cache[key]

    result = unique_paths(m-1, n, cache) + unique_paths(m, n-1, cache)
    cache[key] = result
    return cache[key]


unique_paths(103, 342)  # 28
