# Question 9.2: A variation to the problem asked in Question 9.1 is that, at
# some places there is repair work going on and hence you cannot take those
# routes. Unavailable route information may be given in the form of point
# array (e.g from point (2, 1) to point (3, 1) the route is not available). Write a function that returns the total number of unique ways to go to some point (x,y) from origin (0,0).


# recursive
def count_paths_with_blocks(x, y, blocked_routes):
    """
    x, y: destination cell coordinates
    blocked_routes: set of blocked edges represented as ((x1, y1), (x2, y2))
    """

    # Base case: if starting point reached
    if x == 0 and y == 0:
        return 1

    paths = 0

    # Move from above (x-1, y) -> (x, y) if not blocked
    if x > 0 and ((x-1, y), (x, y)) not in blocked_routes:
        paths += count_paths_with_blocks(x-1, y, blocked_routes)

    # Move from left (x, y-1) -> (x, y) if not blocked
    if y > 0 and ((x, y-1), (x, y)) not in blocked_routes:
        paths += count_paths_with_blocks(x, y-1, blocked_routes)

    return paths

def count_paths_with_blocks_dp(x, y, blocked_routes):
    dp = [[0] * y for _ in range(x)]
    dp[0][0] = 1

    for i in range(x):
        for j in range(y):
            if i > 0 and ((i-1, j), (i, j)) not in blocked_routes:
                dp[i][j] += dp[i-1][j]
            if j > 0 and ((i, j-1), (i, j)) not in blocked_routes:
                dp[i][j] += dp[i][j-1]

    return dp[x-1][y-1]

def total_paths(N, M, blocked_routes):
    """
    Returns number of unique paths from (0,0) to (N-1,M-1)
    blocked_routes should be a set of tuples:
    {((x1, y1), (x2, y2)), ...}
    """
    return count_paths_with_blocks(N-1, M-1, blocked_routes)


M = 4
N = 4

blocked_routes = {
    ((2,1), (3,1)),
    ((1,2), (1,5))
}

print(total_paths(M, N, blocked_routes))
print(count_paths_with_blocks_dp(M, N, blocked_routes))

