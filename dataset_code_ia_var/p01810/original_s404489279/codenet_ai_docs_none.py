n, k = map(int, input().split())
now = 0
while n > 1:
    n -= 1
    now = (now * k) // (k - 1) + 1
print(now)