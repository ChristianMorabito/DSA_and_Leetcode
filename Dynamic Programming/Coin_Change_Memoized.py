def _coin_change_rec(amount: int, coins: set[int], cache=None) -> int:

    # INITIALISE THE CACHE DICTIONARY
    if cache is None:
        cache = {}

    # BASE CASE
    if amount == 0:
        return 0

    # ACCESS CACHE DATA
    if amount in cache:
        return cache[amount]

    min_amt = float('inf')

    for coin in coins:
        if amount - coin >= 0:
            min_amt = min(min_amt, 1 + _coin_change_rec(amount - coin, coins, cache))

    # INSERT CACHE DATA
    cache[amount] = min_amt
    return min_amt


def coin_change(amount: int, coins: set[int]) -> int:
    
    # CALL THE RECURSIVE FUNCTION
    result = _coin_change_rec(amount, coins)
    return result if result != float("inf") else -1


print(coin_change(50, {1, 2}))

