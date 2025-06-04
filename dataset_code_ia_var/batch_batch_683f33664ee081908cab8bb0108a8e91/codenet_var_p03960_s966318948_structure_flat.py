import sys
input = sys.stdin.readline

h, w = map(int, input().split())

c = []
for i in range(w):
    c.append(chr(150 + i))
for i in range(h):
    inp = input()
    for j in range(w):
        c.append(inp[j])

h = h + 1
h2 = h * h
res = 0
j = 1
while j < w:
    d = [0] * h2
    x = 1
    while x < h:
        y = 1
        while y < h:
            if c[x * w + j] == c[y * w + j - 1]:
                d[x * h + y] = d[x * h + y - h - 1] + 1
            else:
                d[x * h + y] = d[x * h + y - h - 1]
            y += 1
        x += 1
    dp = [10 ** 10] * h2
    i = 0
    while i < h:
        dp[i] = 0
        dp[i * h] = 0
        i += 1
    x = 1
    while x < h:
        y = 1
        while y < h:
            a = dp[x * h + y - 1]
            b = dp[x * h - h + y]
            if a < b:
                dp[x * h + y] = a + d[x * h + y]
            else:
                dp[x * h + y] = b + d[x * h + y]
            y += 1
        x += 1
    res = res + dp[-1]
    j += 1

print(res)