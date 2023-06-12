# This BOTTOM-UP algorithm is concise & the technique is elegant once you get your head around it.
# Example inputs: a = 3¢; coins = {2¢, 1¢}
# 1) Create array: dp, filled with float("inf"). Remember, goal is to find min number of coins.
#   i.e. dp = [inf, inf, inf, inf]      <- note: length of array is (amount + 1)
#               ^    ^    ^    ^
#              a=0¢ a=1¢ a=2¢ a=3¢
# The technique is to break the amount into sub-amounts & work up. So instead of finding amount of 3,
# first find the amount of 0, then 1, 2 & then finally 3. The indexes of dp represent an amount, & the values in each
# dp index represent the number of coins.
# E.g. if dp[3] == 2, then that means 2 coins were used to get the amount of 3¢.

# 2) So because an amount of zero requires zero coins, then dp[0] = 0 ; i.e. dp = [0, inf, inf, inf]

# 3) Two 'for loops' are required.
#   The 1st loop is to traverse only once through the 'dp' array, & the 2nd loop is nested within the 1st loop;
#   it loops through the coins set. E.g. dp = [0, inf, inf, inf] <- main loop
#                                                            ^
#                                    coins =               {2¢, 1¢}              <- nested loop
#                                               0  1  2  3
# E.g. [0, 1, inf, inf]  |  [0, 1, 1, inf]  |  [0, 1, 1, 2]
#          ^                       ^                     ^
#      1 coin of 1¢             1 coin of 2¢         2 coins (1 coin of 1¢, & 1 coin of 2¢)


def coin_change_iter(amount: int, coins: set[int]) -> int:
    dp = [float("inf")] * (amount + 1)  # dp [0, 1, 1, 2]
    dp[0] = 0
    for sub_amount in range(1, amount + 1):  # sub_amount = 3
        for coin in coins:  # {1, 2}           coins = 2
            if sub_amount - coin >= 0:  # 3 - 2 = 1
                dp[sub_amount] = min(dp[sub_amount], 1 + dp[sub_amount - coin])
                # dp[3] = 2, 2
    return dp[amount] if dp[amount] != float("inf") else -1


print(coin_change_iter(3, {1, 2}))
