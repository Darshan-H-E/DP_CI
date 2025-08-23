# You are given a n x (n-1) grid, where all cells are 0 or 1. 0 represents light, and 1 represents shade. Starting from (0,0) see if it is possible to reach the opposite diagonal (n-1, n-2) with following 2 conditions:
#
# 1) Only horizontal and vertical movement is allowed
# 2) the number of visits to dark and light cells must be equal. This includes the initial visit to (0,0) and final visit to (n-1, n-2)

def has_equal_light_dark_path(grid):
    n, m = len(grid), len(grid[0])
    target = (n - 1, m - 1)
    memo = {}

    def dfs(x, y, light, dark, visited):
        key = (x, y, light, dark, tuple(sorted(visited)))
        if key in memo:
            return memo[key]

        if (x, y) == target:
            memo[key] = (light == dark)
            return memo[key]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                visited.add((nx, ny))
                if grid[nx][ny] == 0:
                    res = dfs(nx, ny, light + 1, dark, visited)
                else:
                    res = dfs(nx, ny, light, dark + 1, visited)
                visited.remove((nx, ny))
                if res:
                    memo[key] = True
                    return True
        memo[key] = False
        return False

    visited = set([(0, 0)])
    light = 1 if grid[0][0] == 0 else 0
    dark = 1 if grid[0][0] == 1 else 0
    return dfs(0, 0, light, dark, visited)

# Example usage:
example_grid = [
    [0, 0],
    [1, 1],
    [0, 0]
]
print("Path Exists" if has_equal_light_dark_path(example_grid) else "No Valid Path")
