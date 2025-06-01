import sys
INF = 10 ** 18 + 7
input = lambda: sys.stdin.readline().strip()
while True:
    n = int(input())
    if n == 0:
        break
    abc = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        abc.append((a, b, c))
    info = [[INF]*10 for _ in range(10)]
    for i in range(10):
        info[i][i] = 0
    for a, b, c in abc:
        info[a][b] = c
        info[b][a] = c
    for i in range(10):
        for l in range(10):
            for k in range(10):
                if info[l][k] > info[l][i] + info[i][k]:
                    info[l][k] = info[l][i] + info[i][k]
    for i in range(10):
        for l in range(10):
            if info[i][l] == INF:
                info[i][l] = 0
    ans = []
    for i in range(10):
        s = sum(info[i])
        if s != 0:
            ans.append((s, i))
    ans.sort()
    print(ans[0][1], ans[0][0])