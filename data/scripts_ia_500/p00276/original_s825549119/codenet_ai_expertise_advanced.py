for _ in range(int(input())):
    c, a, n = map(int, input().split())
    res = m = min(n, a, c)
    c -= m; a -= m
    cca = min(c // 2, a)
    res += cca
    c -= cca * 2
    res += c // 3
    print(res)