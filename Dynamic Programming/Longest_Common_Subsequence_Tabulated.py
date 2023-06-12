def lcs_tab(str1: str, str2: str) -> int:
    dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


print(lcs_tab('BA', 'XBXA'))
#            j
#            B   A
#        0   0   0
#      X 0   0   0
#   i  B 0   1   1
#      X 0   1   1
#      A 0   1   2
