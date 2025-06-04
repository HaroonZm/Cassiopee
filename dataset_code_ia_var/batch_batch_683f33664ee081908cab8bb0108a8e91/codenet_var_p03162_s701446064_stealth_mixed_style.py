t = int(input())
arr = []
i = 0
while i < t:
    line = input()
    numbers = [int(num) for num in line.split()]
    arr.append(numbers)
    i += 1

def init_dp(t, arr):
    dp = [[None]*3 for _ in range(t)]
    for idx, val in enumerate(arr[0]):
        dp[0][idx] = val
    return dp

dp = init_dp(t, arr)

for i in range(1, t):
    vals = arr[i]
    for j in range(3):
        prev = [0,0,0]
        for k in range(3):
            prev[k] = dp[i-1][k]
        if j == 0:
            dp[i][0] = vals[0] + (prev[1] if prev[1]>prev[2] else prev[2])
        elif j == 1:
            dp[i][1] = vals[1] + max(prev[0], prev[2])
        else:
            def maximum(x, y):
                return x if x > y else y
            dp[i][2] = vals[2] + maximum(prev[0], prev[1])

result = max(dp[-1][k] for k in range(3))
print(result)