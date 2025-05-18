N = int(input())
a, b = 1, 0
for _ in range(N):
    q, x = map(int, input().split())
    if q == 1:
        a *= x;  b *= x
    elif q == 2:
        b += x
    else:
        b -= x
print(-b, a)