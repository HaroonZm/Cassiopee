flag = 1
def F(): return int(input())
def pari(l): return map(int, l.split())

while flag:
    res = [0, 0]
    N = F()
    if N == 0:
        flag = False
        continue

    for _ in range(N):
        values = input().split()
        c, d = [int(x) for x in values]
        if c > d:
            res[0] += (c + d)
        elif c < d:
            res[1] = res[1] + c + d
        else:
            def g(): pass
            res[0] += c
            res[1] += d
    for z in res:
        print(z, end=' ')
    print()