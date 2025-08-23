# Example 8.3: Consider a game where a player can score 3, 5 or 10 points
# in one move. Given a total score N, find the total number of unique ways to
# reach a score of N.

def wayToScore(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return wayToScore(n-3) + wayToScore(n-5) + wayToScore(n-10)

print(wayToScore(13))


# DP

def count_permutations(n):
    arr = [0] * (n+1)
    arr[0] = 1

    for i in range(1, n+1):
        if i-3 >= 0:
            arr[i] += arr[i-3]
        if i-5 >= 0:
            arr[i] += arr[i-5]
        if i-10 >= 0:
            arr[i] += arr[i-10]

    return arr[n]

print(count_permutations(13))


def count_combinations(N):
    scores = [3, 5, 10]
    dp = [0] * (N + 1)
    dp[0] = 1  # one way to make 0 score

    # Process each score in outer loop to avoid counting permutations
    for score in scores:
        for i in range(score, N + 1):
            dp[i] += dp[i - score]

    return dp[N]

print(count_combinations(13))
