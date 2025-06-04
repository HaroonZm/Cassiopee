q = int(input())
for i in range(q):
    c, a, n = map(int, input().split())
    s = 0
    while c > 0 and a > 0 and n > 0:
        s = s + 1
        c = c - 1
        a = a - 1
        n = n - 1
    while c > 0 and a > 0:
        s = s + 1
        c = c - 2
        a = a - 1
    print(s + c // 3)