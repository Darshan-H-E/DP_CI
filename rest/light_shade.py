You are given a n x (n-1) grid, where all cells are 0 or 1. 0 represents light, and 1 represents shade. Starting from (0,0) see if it is possible to reach the opposite diagonal (n-1, n-2) with following 2 conditions:

1) Only horizontal and vertical movement is allowed
2) the number of visits to dark and light cells must be equal. This includes the initial visit to (0,0) and final visit to (n-1, n-2)

from collections import deque

def can_reach_with_equal_light_and_shade(grid):
    n = len(grid)
    m = len(grid[0])
    
    # Start & end
    start = (0, 0)
    end = (n - 1, m - 1)  # but note here m = n-1, so it's (n-1, n-2)
    end = (n - 1, m - 1) if m == n else (n - 1, m - 1)  # just for safety
    end = (n - 1, m - 1)  # actually = (n-1, n-2)

    # Compute starting balance
    start_val = grid[0][0]
    balance = 1 if start_val == 1 else -1  # +1 for 1, -1 for 0

    # BFS
    q = deque()
    q.append((0, 0, balance))
    visited = set()
    visited.add((0, 0, balance))

    # Directions: up, down, left, right
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        i, j, bal = q.popleft()

        # Reached end with equal count?
        if (i, j) == end and bal == 0:
            return True

        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                # Update balance
                new_bal = bal + (1 if grid[ni][nj] == 1 else -1)
                state = (ni, nj, new_bal)
                if state not in visited:
                    visited.add(state)
                    q.append(state)

    return False

grid = [
    [0,0,0],
    [0,0,0]
]


n = 3 
n x n - 1
3 x 2

3 - 1, 3 - 2
2, 1

[
  [0, 0]
  [1, 0]
  [1, 0]
]

print(can_reach_with_equal_light_and_shade(grid))  # True / False
