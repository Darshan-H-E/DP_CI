# Find length of longest substring of a given string of digits,
# such that sum of digits in the first half and second half of the substring is
# same. For example,

# Input: "142124"
# Output: 6
# The whole string is answer, because, sum of first 3 digits = sum of last 3
# digits (1+4+2 - 1+2+4) -

# Input: "9430723"
# Output: 4
# Longest substring with first and second half having equal sum is
# "4307"


# Optimizations:
# if the current substr is not greater than maximum length substr
# then we need not calculate it
#
# substr is of even length so we can jump j by 2

def maxSubstrLen(s):
   n = len(s)
   maxLen = 0

   for i in range(n):
       for j in range(i+1, n, 2):
           length = j - i + 1 
           if maxLen >= length:
               continue

           lSum = 0
           rSum = 0

           for k in range(length//2):
               lSum += int(s[i+k])
               rSum += int(s[i+k+(length//2)])

           if lSum == rSum:
               maxLen = length

   return maxLen

print(maxSubstrLen("9430723"))


s = "9430723"
n = len(s)
dp = [[0] * n for _ in range(n)]

def maxSubstrLenDP(s):
    maxLen = 0

    for i in range(n):
        dp[i][i] = int(s[i])


    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i+length-1
            k = length//2
            # update the dp table cell with lSum and rSum
            dp[i][j] = dp[i][j-k] + dp[j-k+1][j]

            if (length%2 == 0 and dp[i][j-k] == dp[j-k+1][j] and length > maxLen):
                maxLen = length

    return maxLen

print(maxSubstrLenDP(s))
