t = int(input())
for i in range(t):
    c, a, n = map(int, input().split())
    res = 0
    # On forme d'abord autant de groupes (1,1,1) que possible
    m1 = min(c, a, n)
    res += m1
    c -= m1
    a -= m1
    n -= m1

    # On forme des groupes (2,1,0)
    if c >= 2 and a >= 1:
        m2 = min(c // 2, a)
        res += m2
        c -= m2 * 2
        a -= m2

    # Si encore des c, on fait des groupes de 3 (3,0,0)
    if c >= 3:
        m3 = c // 3
        res += m3
        c -= m3 * 3

    print(res)