from functools import reduce

def solve():
    nAB = input().split()
    n = int(nAB[0])
    A = int(nAB[1])
    B = int(nAB[2])

    xx = list(map(int, input().split()))
    res = [B if A*(xx[j]-xx[j-1]) > B else A*(xx[j]-xx[j-1]) for j in range(1, n)]

    s = 0
    for item in res:
        s = s + item

    print(s)

solve()