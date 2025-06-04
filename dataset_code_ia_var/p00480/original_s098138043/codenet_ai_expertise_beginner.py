N = int(input())
number_list = input().split()
numbers = []
for item in number_list:
    numbers.append(int(item))
a = numbers[-1]
numbers.pop(-1)

if numbers[0] == 0:
    N = N - 1
    numbers.pop(0)

dp = []
for i in range(N):
    row = []
    for j in range(21):
        row.append(0)
    dp.append(row)

dp[0][0] = 1

for i in range(N - 1):
    for j in range(21):
        if j + numbers[i] <= 20:
            dp[i + 1][j + numbers[i]] = dp[i + 1][j + numbers[i]] + dp[i][j]
        if j - numbers[i] >= 0:
            dp[i + 1][j - numbers[i]] = dp[i + 1][j - numbers[i]] + dp[i][j]

print(dp[N - 1][a])