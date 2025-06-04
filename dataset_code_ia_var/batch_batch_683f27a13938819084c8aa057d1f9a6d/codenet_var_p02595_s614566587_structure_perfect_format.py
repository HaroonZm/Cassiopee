import math

n, d = map(int, input().split())
cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    s = math.sqrt(a * a + b * b)
    if s <= d:
        cnt += 1
print(cnt)