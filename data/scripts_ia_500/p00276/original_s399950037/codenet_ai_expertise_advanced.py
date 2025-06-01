for _ in range(int(input())):
    c, a, n = map(int, input().split())
    s = min(c, a, n)
    c, a, n = c - s, a - s, n - s
    t = min(c // 2, a)
    c, a = c - 2 * t, a - t
    s += t + c // 3
    print(s)