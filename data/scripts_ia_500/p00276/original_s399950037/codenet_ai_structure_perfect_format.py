q = int(input())
for _ in range(q):
    c, a, n = map(int, input().split())
    s = 0
    while c > 0 and a > 0 and n > 0:
        s += 1
        c -= 1
        a -= 1
        n -= 1
    while c > 0 and a > 0:
        s += 1
        c -= 2
        a -= 1
    print(s + c // 3)