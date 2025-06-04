import sys
from collections import deque
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N, W = map(int, readline().split())
    vs = [0]*N; ws = [0]*N; ms = [0]*N
    for i in range(N):
        vs[i], ws[i], ms[i] = map(int, readline().split())
    V0 = max(vs)
    V = sum(v * min(V0, m) for v, m in zip(vs, ms))
    dp = [W+1]*(V + 1)
    dp[0] = 0
    for i in range(N):
        v = vs[i]; w = ws[i]; m = ms[i]
        c = min(V0, m)
        ms[i] -= c
        for k in range(v):
            que = deque()
            push = que.append
            popf = que.popleft; popb = que.pop
            for j in range((V-k)//v+1):
                a = dp[k + j*v] - j * w
                while que and a <= que[-1][1]:
                    popb()
                push((j, a))
                p, b = que[0]
                dp[k + j*v] = b + j * w
                if que and p <= j-c:
                    popf()
    *I, = range(N)
    I.sort(key=lambda x: ws[x]/vs[x])
    *S, = [(vs[i], ws[i], ms[i]) for i in I]
    ans = 0
    def greedy():
        yield 0
        for i in range(V + 1):
            if dp[i] > W:
                continue
            rest = W - dp[i]
            r = i
            for v, w, m in S:
                m = min(m, rest // w)
                r += m * v
                rest -= m * w
            yield r
    write("%d\n" % max(greedy()))
solve()