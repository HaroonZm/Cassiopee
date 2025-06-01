N, K = map(int, input().split())
S = [-1] * N

# Reading K conditions, mapping positions with given values
for _ in range(K):
    a, b = map(int, input().split())
    S[a-1] = b - 1  # zero-based indexing for convenience

dp = [0] * 9  # DP array for 3x3 states

first, second = S[:2]

# Initialize dp based on the first two values
if first != -1:
    if second != -1:
        dp[first * 3 + second] = 1
    else:
        # second unknown, set all possibilities for second
        dp[first * 3 : first * 3 + 3] = [1, 1, 1]
elif second != -1:
    # first unknown, second known
    for i in range(3):
        dp[i * 3 + second] = 1
else:
    # both unknown, all states possible
    dp = [1] * 9

for i in range(2, N):
    cur_val = S[i]
    new_dp = [0] * 9

    if cur_val != -1:
        # Only one possible value for current
        for prev in range(3):
            # sum dp for previous rows where second element == prev
            total = sum(dp[prev::3])
            # Avoid same consecutive values (?), unclear logic from original
            if cur_val == prev:
                new_dp[prev * 3 + cur_val] = total - dp[cur_val * 4]  # dp[cur_val*4] is dp[cur_val*3 + cur_val]?
            else:
                new_dp[prev * 3 + cur_val] = total
    else:
        # current value unknown, try all 3 possibilities
        for cur_val_candidate in range(3):
            for prev in range(3):
                total = sum(dp[prev::3])
                if cur_val_candidate == prev:
                    new_dp[prev * 3 + cur_val_candidate] = total - dp[cur_val_candidate * 4]
                else:
                    new_dp[prev * 3 + cur_val_candidate] = total

    dp = new_dp[:]

print(sum(dp) % 10000)