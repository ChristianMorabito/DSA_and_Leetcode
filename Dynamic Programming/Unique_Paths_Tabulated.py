# Once you know the pattern, this problem is really simple.
# Step 1) Create the m*n matrix named dp. Fill the matrix with 1s
# Example: m=7; n=3; dp = 1   1   1   1   1   1   1
#                         1   1   1   1   1   1   1
#                         1   1   1   1   1   1   1
#
# Step 2) Ignore the 1st column & 1st row; leave it filled with 1s. Now start iterating through each row,
#         adding the previous row/column to the current row column. Again - leave 1st row/column filled with just 1s
#         Example:   dp = 1   1   1   1   1   1   1
#                         1   2   3   4   5   6   7   <-1+1=2,    1+2=3,     1+3=4,      1+4=5,     1+5=6,    1+6=7
#                         1   3   6   10  15  21  28  <-1+2=3,    3+3=6,     6+4=10,     10+5=15,   15+6=21,  21+7=28

# Time: O(n*m); Space: O(n)
def unique_paths(m: int, n: int) -> int:
    dp = [[1]*m] * n
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


print(unique_paths(7, 3))
