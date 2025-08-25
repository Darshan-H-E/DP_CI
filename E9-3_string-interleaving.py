# Example 9.3: String C is said to be interleaving of string A and B if it
# contains all the characters of A and B and the relative order of characters of
# both the strings is preserved in C. For example, if values of A, B and C are
# as given below.
#
# A = xyz B = abcd
# C = xabyczd


def is_interleaved_recursive(str1, str2, str3):
    if (not str1) and (not str2) and (not str3):
        return True

    if not str3:
        return False

    if not str1 and not str2:
        return False

    if len(str3) != len(str1) + len(str2):
        return False
    
    first = False
    second = False

    if len(str1) > 0 and str1[0] == str3[0]:
        first = is_interleaved_recursive(str1[1:], str2, str3[1:])

    if len(str2) > 0 and str2[0] == str3[0]:
        second = is_interleaved_recursive(str1, str2[1:], str3[1:])
    
    return first or second

    
print(is_interleaved_recursive("xyz", "abcd", "xabyczd"))


def is_interleaved_dp(s1, s2, s3):
    m = len(s1)
    n = len(s2)
    o = len(s3)

    if m+n != o:
        return False

    dp = [[False] * n for _ in range(m)]
    dp[0][0] = True

    # populate first column
    for i in range(1, m):
        if s1[i-1] != s3[i-1]:
            dp[i][0] = False
        else:
            dp[i][0] = dp[i-1][0]

    # populate first row
    for j in range(1, n):
        if s2[j-1] != s3[j-1]:
            dp[0][j] = False
        else:
            dp[0][j] = dp[0][j-1]
    
    for i in range(1, m):
        for j in range(1, n):
            # current char is same as s1 not same as s2
            if s1[i-1] == s3[i+j-1] and s2[j-1] != s3[i+j-1]:
                dp[i][j] = dp[i-1][j]

            # current char is same as s2 not same as s1
            elif s1[i-1] != s3[i+j-1] and s2[j-1] == s3[i+j-1]:
                dp[i][j] = dp[i][j-1]

            # current char is same as s2 and s1
            elif s1[i-1] == s3[i+j-1] and s2[j-1] == s3[i+j-1]:
                dp[i][j] = dp[i-1][j] or dp[i][j-1]

            else:
                dp[i][j] = False

    return dp[m-1][n-1]

print(is_interleaved_dp("xyz", "abcd", "xabyczd"))
