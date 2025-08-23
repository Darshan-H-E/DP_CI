# https://chatgpt.com/s/t_68a616eafbf081918a42fcc0b82b2e79

# C(n,k)=C(n−1,k−1)+C(n−1,k)

# Why This Is Natural
# This reasoning is just like making a yes/no decision for each element:
# “Do I take this item?” → Yes or No.
# Each decision reduces the problem to a smaller set, and we keep adding possibilities.
# This is also why Pascal’s Triangle works – each number is the sum of the two numbers above it.

# Key Insight
# The recurrence comes from:
# Splitting the problem into smaller subproblems.
# Considering the inclusion or exclusion of one specific item.

def recursive_comb(n, m):
    if n == 0 or m == 0 or n==m:
        return 1
    return recursive_comb(n-1, m-1) + recursive_comb(n-1, m)
