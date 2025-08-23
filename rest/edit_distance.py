# Example 9.1: The words COMPUTER and COMMUTER are very similar, and
# a update of just one letter, P->M will change the first word into the
# second. Similarly, word SPORT can be changed into SORT by deleting one
# character, p, or equivalently, SORT can be changed into SPORT by
# inserting p.
#
#
# Edit distance between two strings is defined as the minimum number
# of character operations (update, delete, insert) required to convert one
# string into another.
#
# Given two strings strl and str2 and following three operations that
# can performed on str1.
#
# 1. Insert
# 2. Remove
# 3. Replace
#
# Find minimum number of operations requited to convert str1 to str2.


# recursive (2^n)
def edit_distance(str1, str2):
    if not str1:
        return len(str2)

    if not str2:
        return len(str1)

    if str1[0] == str2[0]:
        return edit_distance(str1[1:], str2[1:])

    d = edit_distance(str1[1:], str2)
    u = edit_distance(str1[1:], str2[1:])
    i = edit_distance(str1, str2[1:])

    return min(d, u, i) + 1

# dp (n^2)

def edit_distanceDP(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0] * (n+1) for _ in range(m+1)]

    # left column
    for i in range(m+1):
        dp[i][0] = i

    # top row
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] 
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],
                    dp[i][j-1],
                    dp[i-1][j-1]
                )

    return dp[m][n]

