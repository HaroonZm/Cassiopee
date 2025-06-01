n = int(input())
s = []
for _ in range(n):
    line = input()
    parts = line.split()
    c = int(parts[0])
    w = int(parts[1])
    s.append((c, w))

p = []
for i in range(n + 1):
    row = []
    for j in range(n + 1):
        if i == j:
            row.append(True)
        else:
            row.append(False)
    p.append(row)

c = [0]
w = [0]
for pair in s:
    c.append(pair[0])
    w.append(pair[1])

sum_w = [0]
for i in range(1, n + 1):
    sum_w.append(sum_w[i - 1] + w[i])

for length in range(n):
    for i in range(1, n + 1 - length):
        j = i + length
        if p[i][j]:
            if j + 1 <= n:
                if sum_w[j] - sum_w[i - 1] <= c[j + 1]:
                    p[i][j + 1] = True
            if i - 1 >= 0:
                if sum_w[j] - sum_w[i - 1] <= c[i - 1]:
                    p[i - 1][j] = True

dp = [10**9] * (n + 1)
dp[0] = 0

for b in range(1, n + 1):
    for e in range(1, n + 1):
        if p[b][e]:
            if dp[b - 1] + 1 < dp[e]:
                dp[e] = dp[b - 1] + 1

print(dp[n])