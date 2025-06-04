import sys

d, n = map(int, input().split())
temperatures = []
for _ in range(d):
    temperatures.append(int(input()))
clothes = []
for _ in range(n):
    clothes.append(list(map(int, input().split())))

points = []
for i in range(len(temperatures)):
    row = []
    for c in clothes:
        if c[0] <= temperatures[i] <= c[1]:
            row.append(c[2])
    row.sort()
    points.append(row)

if len(points[0]) == 1:
    dp = [[points[0][0], 0], [points[0][0], 0]]
else:
    dp = [[points[0][0], 0], [points[0][-1], 0]]

for i in range(1, len(points)):
    p = points[i]
    min_p = p[0]
    max_p = p[-1]
    a1 = max(
        dp[0][1] + abs(min_p - dp[0][0]),
        dp[1][1] + abs(min_p - dp[1][0])
    )
    a2 = max(
        dp[0][1] + abs(max_p - dp[0][0]),
        dp[1][1] + abs(max_p - dp[1][0])
    )
    dp = [[min_p, a1], [max_p, a2]]

ans = max(dp[0][1], dp[1][1])
print(ans)