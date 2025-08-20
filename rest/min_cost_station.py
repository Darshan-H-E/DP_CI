# There are n stations in a route, starting from 0 to n-1.
#  A train moves from first station 0 to last station n-1 in
#  only forward direction. The cost of ticket b/w 2 stations
#  is given. Find the min cost of travel from station 0 to n-1

# cost matrix
# [
#     [0, 10, 75, 94]
#     [-1, 0, 35, 50]
#     [-1, -1, 0, 80]
#     [-1, -1, -1, 0]
# ]
#

# algorithm
# minCost(0, n-1) = min {
#             cost[0][n-1],
#             cost[0][1] + minCost(1, n-1),
#             cost[0][2] + minCost(2, n-1),
#             ...,
#             minCost(0, n-2) + cost[n-2][n-1]
#         }


# Terminating conditions
# if (s == d):
#     return 0
#
# if (s == d-1):
#     return  cost[s][d]

# cost = [[0 for _ in range(n)] for _ in range(n)]

cost = [
    [0, 10, 75, 94],
    [-1, 0, 35, 50],
    [-1, -1, 0, 80],
    [-1, -1, -1, 0],
]

def calculateMinCost(s, d):
    if (s == d or s == d-1):
        return cost[s][d]
    
    minCost = cost[s][d]

    for i in range(s+1, d):
        temp = calculateMinCost(s, i) + calculateMinCost(i, d)
        if temp < minCost:
            minCost = temp

    return minCost

## Memo
memo = [[-1] * len(cost) for _ in range(len(cost))]

def calculateMemoMinCost(s, d):
    if (s == d or s == d-1):
        return cost[s][d]
    
    
    if memo[s][d] == -1:
        minCost = cost[s][d]

        for i in range(s+1, d):
            temp = calculateMemoMinCost(s, i) + calculateMemoMinCost(i, d)
            if temp < minCost:
                minCost = temp
        memo[s][d] = minCost
    return memo[s][d]

print(calculateMinCost(0, 2))
print(calculateMemoMinCost(0, 2))

def calculateIterMinCost(d):
    n = len(cost)
    minCost = [0] * n
    minCost[0] = 0
    minCost[1] = cost[0][1]

    for i in range(2, n):
        minCost[i] = cost[0][i]

        for j in range(1, i):
            if minCost[i] > minCost[j] + cost[j][i]:
                minCost[i] = minCost[j] + cost[j][i]

    return minCost[d]

print(calculateIterMinCost(2))

