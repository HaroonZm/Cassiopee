n = int(input())
a, b = 0, 1

for _ in range(n):
    q, x = map(int, input().split())
    if q == 1:
        a, b = a * x, b * x
    elif q == 2:
        a = a + b * x
    else:  # q == 3
        a = a - b * x

print(-a, b)