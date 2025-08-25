# Question 9.4: Minimum Chess Moves Problem. In the game of chess a
# Knight can move 2.5 steps (a square that can be reached by moving two
# squares horizontally and one square vertically, or two squares vertically and
# one squate horizontally). Picture 9.9 shows all possible moves of a knight.
# A King, can move only one step (either horizontally, vertically or
# diagonally).
#
# We have designed a special piece that can move either like a knight or
# like a king. Given that P is in a particular cell, and you want to move it to another
# cell then what is the minimum number of moves it takes P to go from
# source to destination. Write a function that accepts source and destination
# cells and return the minimum number of moves it will take P to move from
# source to destination cell.

from collections import deque

# BFS
def min_chess_moves_bfs(N, M, src, dest):
    # Possible moves
    knight_moves = [(2,1), (2,-1), (-2,1), (-2,-1),
                    (1,2), (1,-2), (-1,2), (-1,-2)]
    king_moves = [(1,0), (-1,0), (0,1), (0,-1),
                  (1,1), (1,-1), (-1,1), (-1,-1)]
    
    moves = knight_moves + king_moves  # Combine both
    
    visited = [[False]*M for _ in range(N)]
    queue = deque()
    queue.append((src[0], src[1], 0))  # (x, y, steps)
    visited[src[0]][src[1]] = True

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == dest:
            return steps

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))

    return -1  # Destination not reachable

print(min_chess_moves_bfs(8, 8, (0, 0), (7, 7)))

# Recursive DFS with memoization (Recursion depth exceeded)
# def min_chess_moves_recursive(N, src, dest, memo=None):
#
#     if memo is None:
#         memo = {}
#
#     # Base case: already at destination
#     if src == dest:
#         return 0
#
#     if src in memo:
#         return memo[src]
#
#     x, y = src
#
#     # All possible knight moves
#     knight_moves = [
#         (2, 1), (2, -1), (-2, 1), (-2, -1),
#         (1, 2), (1, -2), (-1, 2), (-1, -2)
#     ]
#
#     # All possible king moves
#     king_moves = [
#         (1, 0), (-1, 0), (0, 1), (0, -1),
#         (1, 1), (1, -1), (-1, 1), (-1, -1)
#     ]
#
#     moves = knight_moves + king_moves
#     min_steps = float('inf')
#
#     for dx, dy in moves:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < N and 0 <= ny < N:
#             steps = 1 + min_chess_moves_recursive(N, (nx, ny), dest, memo)
#             min_steps = min(min_steps, steps)
#
#     memo[src] = min_steps
#     return min_steps
#
# print(min_chess_moves_recursive(8, (0, 0), (7, 7)))


# DP approach using BFS to fill minimum moves table.

def min_chess_moves_dp(N, src, dest):
    if src == dest:
        return 0

    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    king_moves = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    moves = knight_moves + king_moves

    # DP table initialized to large value
    dp = [[float('inf')] * N for _ in range(N)]
    dp[src[0]][src[1]] = 0  # starting cell requires 0 moves

    # BFS queue
    queue = deque([src])

    while queue:
        x, y = queue.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if dp[nx][ny] > dp[x][y] + 1:
                    dp[nx][ny] = dp[x][y] + 1
                    queue.append((nx, ny))

    return dp[dest[0]][dest[1]]

# Example
print(min_chess_moves_dp(8, (0, 0), (7, 7)))
