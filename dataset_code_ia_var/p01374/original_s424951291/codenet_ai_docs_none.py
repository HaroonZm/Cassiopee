from collections import deque, defaultdict
import sys
readline = sys.stdin.readline
write = sys.stdout.write

ca = ord('a')
class AhoCorasick:
    def __init__(self):
        self.root = root = [None]*30
        root[-2] = 0; root[-3] = 0
        root[-4] = 0
        self.nodes = [root]

    def add(self, s):
        node = self.root
        nodes = self.nodes
        for c in s:
            code = ord(c) - ca
            child = node[code]
            if not child:
                node[code] = child = [None]*30
                child[-2] = node[-2] + 1
                child[-3] = 0
                child[-4] = len(nodes)
                nodes.append(child)
            node = child
        node[-3] = 1

    def suffix(self):
        root = self.root
        que = deque([root])
        while que:
            v = que.popleft()
            if v[-1]:
                v[-3] += v[-1][-3]
            for i in range(26):
                if not v[i]:
                    if v[-1]:
                        v[i] = v[-1][i]
                    else:
                        v[i] = root[i] or root
                    continue
                if v[-1]:
                    v[i][-1] = v[-1][i]
                else:
                    v[i][-1] = root
                que.append(v[i])
        root[-1] = root

def solve():
    MOD = 10**9 + 7
    N, M, K = map(int, readline().split())
    if N == M == K == 0:
        return False
    mp = {}
    G = []
    S = []
    cur = 0
    fc = lambda x: ord(x) - ca
    for i in range(N):
        f, t = readline().strip().split()
        if f not in mp:
            mp[f] = cur
            G.append([])
            S.append(list(map(fc, f)))
            cur += 1
        if t not in mp:
            mp[t] = cur
            G.append([])
            S.append(list(map(fc, t)))
            cur += 1
        G[mp[f]].append(mp[t])
    *LS, = map(len, S)
    tree = AhoCorasick()
    for i in range(K):
        s = readline().strip()
        tree.add(s)
    tree.suffix()
    L = len(S)
    K = len(tree.nodes)
    G0 = [[None]*L for i in range(K)]
    for k in range(K):
        nd0 = tree.nodes[k]
        g = G0[k]
        for i in range(L):
            s = S[i]
            if len(s) > M:
                continue
            nd = nd0
            c = 0
            for e in s:
                nd = nd[e]
                c += nd[-3]
            if c <= 1:
                g[i] = (nd[-4], c)

    dp = [defaultdict(int) for i in range(M+1)]
    root = tree.root
    v0 = root[-4]
    for i in range(L):
        e = G0[v0][i]
        if e is None:
            continue
        w, c = e
        dp[LS[i]][i, w, c] = 1
    for i in range(M):
        for (v, p, c0), v0 in dp[i].items():
            v0 %= MOD
            g = G0[p]
            for w in G[v]:
                e = g[w]
                if e is None or i+LS[w] > M:
                    continue
                q, c = e
                if c0+c <= 1:
                    dp[i+LS[w]][w, q, c0+c] += v0
    ans = 0
    for (v, p, c0), v0 in dp[M].items():
        if c0 == 1:
            ans += v0
    write("%d\n" % (ans % MOD))
    return True
while solve():
    ...