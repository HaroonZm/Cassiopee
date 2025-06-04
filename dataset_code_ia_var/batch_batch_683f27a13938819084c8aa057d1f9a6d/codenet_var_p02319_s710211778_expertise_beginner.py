N, W = map(int, input().split())
items = []
for i in range(N):
    v, w = map(int, input().split())
    items.append([v, w])

max_value = 0
for item in items:
    max_value += item[0]

dp = [W+1] * (max_value + 1)
dp[0] = 0

for item in items:
    v = item[0]
    w = item[1]
    j = max_value
    while j >= v:
        if dp[j-v] + w < dp[j]:
            dp[j] = dp[j-v] + w
        j -= 1

i = max_value
while i >= 0:
    if dp[i] <= W:
        print(i)
        break
    i -= 1