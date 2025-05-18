# https://tjkendev.github.io/procon-library/python/graph/scc.html
# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

N, M = map(int, input().split())
E1 = [[] for _ in range(N+1)]
E2 = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    E1[a].append(b)
    E2[b].append(a)
label, group = scc(N+1, E1, E2)
for g in group[1:]:
    ans = []
    for n, gg in enumerate(group[1:], 1):
        if g == gg:
            ans.append(n)
    print(" ".join(map(str, ans)))