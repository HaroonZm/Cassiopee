while 1:
    b, r, g, c, s, t = map(int, input().split())
    if t == 0:
        break
    ans = 100
    ans += 13 * (5 * b) + 12 * b
    t -= 6 * b
    ans += 13 * (3 * r) + 12 * r
    t -= 4 * r
    ans += 4 * g
    t -= g
    ans += -1 * c
    t -= c
    t -= s
    ans += -3 * t
    print(ans)