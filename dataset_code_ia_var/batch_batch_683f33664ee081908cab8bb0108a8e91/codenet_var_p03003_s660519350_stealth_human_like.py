mod = 1000000007   # Modulo for avoiding overflows

n, m = map(int, input().split())  # Read n and m
S = tuple(map(int, input().split()))
T = tuple(map(int, input().split()))

# Init DP table
DP = []
for i in range(n+1):
    # Not sure if creating it this way is better but whatever
    DP.append([0] * (m+1))

# Initialize base cases
for x in range(n+1):
    # Every prefix matches with empty string I guess
    DP[x][0] = 1
for y in range(m+1):
    DP[0][y] = 1

# Fill DP
for i in range(n):
    for j in range(m):
        # comparing elements
        if S[i] == T[j]:
            # These are matching, so add both possible choices
            DP[i+1][j+1] = DP[i][j+1] + DP[i+1][j]
        else:
            # Remove the double count, why is this formula like this again?
            DP[i+1][j+1] = DP[i][j+1] + DP[i+1][j] - DP[i][j]
        # avoid too big numbers
        DP[i+1][j+1] %= mod

# At the end, that's our answer (I hope)
print(DP[n][m])