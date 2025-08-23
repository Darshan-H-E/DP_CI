# Example 8.1: Given a two-dimensional square matrix cost [] [] of order
# M*N where cost[i][j] represents the cost of passing though cell (i, j).
# Total cost to reach a particular cell is the sum of costs of all the cells in that
# path (including the starting and final cell. We can only move either
# downward or rightward. i.e If we are at cell (i, j) then we can either go
# to cell (i, j+1) orto (i+1, j).
#
# Write a function that return the minimum cost of moving from the
# top-left cell to bottom-right cell of the matrix.


# Recursive solution 
def minPathCost(costMatrix, m, n):
    if m == 0 and n == 0:
        return costMatrix[0][0]
    if m == 0:
        return minPathCost(costMatrix, m, n-1)  + costMatrix[0][n]
    if n == 0:
        return minPathCost(costMatrix, m-1, n) + costMatrix[m][0]

    x = minPathCost(costMatrix, m-1, n)
    y = minPathCost(costMatrix, m, n-1)
    return (min(x,y) + costMatrix[m][n])

# If values of M and N are large, there will be lot of overlaps and as
# expected, Above Code 8.2 takes exponential time, O(2^n) . And since it involves
# recursion, the extra memory taken is also very high.


# Recursive + Memoization solution
costMatrix = [[]]
memo = [[0] * m for m in range(len(costMatrix))]
def minPathMemoCost(costMatrix, m, n):
    if memo[m][n] != 0:
        return memo[m][n]

    if m == 0 and n == 0:
        memo[m][n] = costMatrix[0][0]

    if m == 0:
        memo[m][n] = minPathMemoCost(costMatrix, m, n-1)  + costMatrix[0][n]
    if n == 0:
        memo[m][n] = minPathMemoCost(costMatrix, m-1, n) + costMatrix[m][0]

    x = minPathMemoCost(costMatrix, m-1, n)
    y = minPathMemoCost(costMatrix, m, n-1)
    memo[m][n] = (min(x,y) + costMatrix[m][n])

    return memo[m][n]

# Compare it with Picture 8.2. Total number of function calls have
# reduced substantially. Time taken by Code 8.3 is O(n^2). If we consider a
# larger matrix (of say, 100*100), then the difference between recursion and
# memoization is huge.


# DP (bottom up approach)
dp = [[]]
def minPathDPCost(costMatrix):
    dp[0][0] = costMatrix[0][0]
    m = len(costMatrix)
    n = len(costMatrix[0])

    # Left column
    for i in range(m):
        dp[i][0] = dp[i-1][0] + costMatrix[i][0]

    # Top row
    for j in range(n):
        dp[0][j] = dp[0][j-1] + costMatrix[0][j]

    for i in range(m):
        for j in range(n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + costMatrix[i][j]

    return dp[m-1][n-1]

# Code 8.4 does not use recursion and takes O (n^2) time. It is a huge
# improvement over previous two versions, recursion and memoization.
