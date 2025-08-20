# Given a matrix of order N*N. What are the total number of
# ways in which we can move from the top-left cell (arr [0] [0]) to the
# bottom-right cell (arr [N-1] [N-1]), given that we can only move either
# downward or rightward?

import math

def count_paths_formula(N: int) -> int:
    return math.comb(2*N-2, N-1)


def count_paths_dp(N: int) -> int:
    dp = [[0] * N for _ in range(N)]  # First row and col = 1

    for i in range(N):
        dp[i][0] = 1
    for j in range(N):
        dp[0][j] = 1

    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[N - 1][N - 1]


N = 4
print("Paths (combinatorics):", count_paths_formula(N))
print("Paths (DP):", count_paths_dp(N))
