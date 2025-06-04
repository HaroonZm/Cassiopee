import sys
sys.setrecursionlimit(10**7)

# 入力読み取り
p = float(input())  # 辺を遷移する確率
N = int(input())    # 頂点数

# 木の構築
# グラフを子のリストとして保持（1を根とした木）
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y, c = map(int, input().split())
    # 双方向に重み付き辺を保存
    graph[x].append((y, c))
    graph[y].append((x, c))

# root=1を根とした木の形に変換し、
# 親方向の辺は除いて子だけを保存
children = [[] for _ in range(N+1)]
visited = [False]*(N+1)
def build_tree(u):
    visited[u] = True
    for v,c in graph[u]:
        if not visited[v]:
            children[u].append((v,c))
            build_tree(v)
build_tree(1)

# 問題のフラクタル木T'の定義：
# T'は、Tの各頂点xに対して、
# xを根とするTと同じ形（同じコストを持つ）木を再帰的に付け加えた木である。

# 探索時、確率pで子に遷移し、1-pで遷移しない。
# これを繰り返すので、T'のDFSの遷移の期待値を計算したい。

# 状態DPを定義すると以下の再帰式になる。
# f(x) := 頂点xを根とするT'のDFSにおいて、
#        頂点xから出発して訪問する全ての辺のコストの期待値
# xの各子cについて、
# 1) x->cの辺を遷移するかどうかは確率pであり、
# 2) 遷移すると、コストc_が加わり、
#    さらに子cの根とするT'に対する期待値f(c)が加わる。
#
# よって、
# f(x) = Σ_{c: child of x} p * (cost(x,c) + f(c))

# 再帰関数で計算
def dfs(x):
    res = 0.0
    for c, cost in children[x]:
        res += p * (cost + dfs(c))
    return res

answer = dfs(1)

# 出力誤差10^-6以下でよいので浮動小数点で十分
print(answer)