import sys

INF = int(1e9)

def dfs(g, u):
    res = 1 << u
    for v in g[u]:
        res |= dfs(g, v)
    return res

def main():
    while True:
        inp = sys.stdin.readline()
        if not inp:
            break
        t = inp.strip().split()
        if not t:
            continue
        n, m = map(int, t)
        if n == 0 and m == 0:
            break
        cs = [0]*20
        g = [[] for _ in range(n)]
        for i in range(n):
            arr = sys.stdin.readline().split()
            cs[i] = int(arr[0])
            k = int(arr[1])
            g[i] = list(map(int, arr[2:2+k]))
        bs = [0]*20
        for i in range(n):
            bs[i] = dfs(g, i)
        sums = [0]*(1<<20)
        for i in range(n):
            sums[1<<i] = cs[i]
        for i in range(1<<n):
            lowbit = i & -i
            if i == 0:
                continue
            sums[i] = sums[lowbit] + sums[i - lowbit]
        res = INF
        for i in range(1<<n):
            if bin(i).count('1') >= res:
                continue
            b = 0
            for j in range(n):
                if (i >> j) & 1:
                    b |= bs[j]
            if sums[b] >= m:
                res = min(res, bin(b).count('1'))
        print(res)

main()