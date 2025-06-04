import sys
readline = sys.stdin.readline
write = sys.stdout.write

D = [
    (2, 1, 5, 0, 4, 3),  # 'L'
    (1, 5, 2, 3, 0, 4),  # 'U'
    (3, 1, 0, 5, 4, 2),  # 'R'
    (4, 0, 2, 3, 5, 1),  # 'D'
]

def rotate_dice(L, k):
    return [L[e] for e in D[k]]

dd = ((-1, 0), (0, -1), (1, 0), (0, 1))

def solve():
    D = "LBRF"

    N = int(readline())
    if N == 0:
        return False

    PS = []
    memo = [-1] * (1 << N)

    def dfs(state, us):
        res = 0
        if memo[state] != -1:
            return memo[state]
        for i in range(N):
            if state & (1 << i):
                continue
            vs = set(us)
            r = 0
            for x, y, e in PS[i]:
                k = (x, y)
                if k in vs:
                    continue
                vs.add(k)
                r += e
            res = max(res, dfs(state | (1 << i), vs) + r)
        memo[state] = res
        return res

    for i in range(N):
        x, y = map(int, readline().split())
        y = -y
        l, r, f, b, d, u = map(int, readline().split())
        L = [u, f, r, l, b, d]
        s = readline().strip()
        P = [(x, y, d)]
        for e in map(D.index, s):
            dx, dy = dd[e]
            L = rotate_dice(L, e)
            x += dx
            y += dy
            P.append((x, y, L[-1]))
        P.reverse()
        PS.append(P)
    write("%d\n" % dfs(0, set()))
    return True

while solve():
    ...