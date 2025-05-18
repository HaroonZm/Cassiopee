# サイクル検出
import sys
sys.setrecursionlimit(10**7) 

def dfs(G, v, p):
    global pos
    seen[v] = True
    hist.append(v)
    for nv in G[v]:
        # 逆流を禁止する
        if nv == p:
            continue

        # 完全終了した頂点はスルー
        if finished[nv]:
            continue

        # サイクルを検出
        if seen[nv] and not finished[nv]:
            pos = nv
            return
        
        # 再帰的に探索
        dfs(G, nv, v)

        # サイクル検出したならば真っ直ぐに抜けていく
        if pos != -1:
            return 
    hist.pop()
    finished[v] = True

# 頂点数 (サイクルを一つ含むグラフなので辺数は N で確定)
N = int(input())

# グラフ入力受取
G = [[] for _ in range(N)]
for i in range(N):
    a,b = map(int, input().split())
    # 頂点番号が 1-indexed で与えられるので 0-indexed にする
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

# 探索
seen = [False]*N
finished = [False]*N
pos = -1
hist = []
dfs(G, 0, -1)

# サイクルを復元
cycle = set()
while len(hist):
    t = hist.pop()
    cycle.add(t)
    if t == pos:
        break

# クエリに答える
Q = int(input())
for _ in range(Q):
    a,b = map(int, input().split())
    a-=1
    b-=1
    if a in cycle and b in cycle:
        print(2)
    else:
        print(1)