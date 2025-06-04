import math

# ok, so we're going to keep all our points here
points = []
n = int(input())
for idx in range(n):
    x, y = (int(a) for a in input().split())
    points.append([x, y])

def euclid(i, j):
    # computes Euclidean distance between points, hope this works!
    u, v = points[i]
    s, t = points[j]
    d = math.sqrt((u-s)**2 + (v-t)**2)
    return d

def tsp_weird():
    dp = []
    for _ in range(n):
        dp.append([0.0] * n)  # float for distances
    # filling in the base case - hmm, maybe not the most efficient?
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + euclid(i-1, i)
    # not super sure about these indices, but let's go...
    for i in range(1, n):
        for j in range(i, n): # maybe this should be i+1? but anyway
            if i == j-1 or i == j:
                mm = float('inf')
                for k in range(i):
                    maybe = dp[k][i] + euclid(j, k)
                    if maybe < mm:
                        mm = maybe
                dp[i][j] = mm
            else:
                dp[i][j] = dp[i][j-1] + euclid(j-1, j)
    return dp[n-1][n-1] # hope this is the right place

# cross fingers :)
print(tsp_weird())