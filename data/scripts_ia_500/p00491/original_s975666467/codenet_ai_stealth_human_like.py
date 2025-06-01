N, K = map(int, input().split())
S = [0] * N

# Reading the fixed values
for _ in range(K):
    a, b = map(int, input().split())
    S[a - 1] = b  # storing at zero-based index

dp = [0] * 9
first, second = S[:2]

# Setting initial dp states based on first two elements
if first:
    if second:
        # both known
        dp[(first - 1) * 3 + (second - 1)] = 1
    else:
        # first known, second unknown
        for j in range(3):
            dp[(first - 1) * 3 + j] = 1
elif second:
    # first unknown, second known
    for i in range(3):
        dp[i * 3 + (second - 1)] = 1
else:
    # both unknown
    dp = [1] * 9

# Now fill dp for remaining positions
for i in range(2, N):
    curr = S[i] - 1
    new_dp = [0] * 9
    if curr != -1:
        # current known
        for prev in range(3):
            # sum over previous states with different prev color
            total = sum(dp[prev * 3:(prev + 1) * 3])
            # subtract if prev color equals curr color at diagonal
            if prev == curr:
                total -= dp[prev * 3 + curr]
            new_dp[prev * 3 + curr] = total
    else:
        # current unknown
        for curr_color in range(3):
            for prev in range(3):
                total = sum(dp[prev * 3:(prev + 1) * 3])
                if prev == curr_color:
                    total -= dp[prev * 3 + curr_color]
                new_dp[prev * 3 + curr_color] = total
    dp = new_dp

print(sum(dp) % 10000)