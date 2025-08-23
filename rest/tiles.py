# Example 8.2: Given an empty plot of size 2 x n. We want to place tiles
# such that the entire plot is covered. Each tile is of size 2 x 1 and can be
# placed either horizontally or vertically. If n is 5, then one way to cover the
# plot is as shown in Picture 8.6
# Write a function that accept n as input and return the total number of
# ways in which we can place the tiles (without breaking any tile).


def ways_to_place_tiles(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    return ways_to_place_tiles(n-1) + ways_to_place_tiles(n-2)


# Question 8.2: If size of the plot in Example 8.2 is changed to 3*n, then
# what changes do we need to make in the solution? Picture 8.9 shows one of
# the possible arrangements on a plot of size 3*n where n=12.

from functools import lru_cache

def count_ways_3xn(n):
    @lru_cache(None)
    def dp(col, mask):
        # Base case: all columns filled
        if col == n:
            return 1 if mask == 0 else 0

        # If column is already fully filled, move to next
        if mask == 0:
            return sum(dp(col, new_mask) for new_mask in transitions[mask])
        
        # Otherwise fill based on transitions
        total = 0
        for next_mask in transitions[mask]:
            total += dp(col + 1, next_mask)
        return total

    # Precomputed transitions for 3-cell states
    transitions = {
        0: [0, 3, 6],  # example transitions for empty column
        1: [2, 5],
        2: [1, 4],
        3: [0, 3, 6],
        4: [2, 5],
        5: [1, 4],
        6: [0, 3, 6],
        7: []  # fully blocked - invalid
    }

    return dp(0, 0)

print(count_ways_3xn(12))
