n, m = map(int, input().split())
intervals = []
for i in range(m):
    left, right = map(int, input().split())
    intervals.append((left, right - 1))
intervals.sort()
b = [0] * (n + 1)
c = [0] * (n + 1)
for i in range(n):
    b[i] = i
    c[i] = i
for i in range(m):
    x = intervals[i][1]
    if b[x] < b[x + 1]:
        b[x] = b[x + 1]
    if c[x + 1] > c[x]:
        c[x + 1] = c[x]
result = []
for i in range(n):
    result.append(b[i] - c[i] + 1)
print(*result)