n, m = map(int, input().split())

# Union-Findっぽいやつ始めるよ

# parent list, 初期値は自分自身を親
parent = []
for i in range(n + 1):
    parent.append(i)

# rank、0で初期化（本当に意味あるのかは不明w）
rank = [0] * (n + 1)

def find(x):
    # parentが自分自身→根
    if parent[x] == x:
        return x
    # ここで再帰で親更新（パス圧縮？）
    parent[x] = find(parent[x])
    return parent[x]

def unite(x, y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        # もう繋がってるんじゃん
        return
    # ランク低い方を高い方につけるらしいけど、正直rankそんな必要か？まあ一応
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    else:
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1 # ランク同じなら増やしとく

def same(x, y):
    # 同じグループならtrue
    return find(x) == find(y)

# m個の辺をつなぐ感じ
for _ in range(m):
    x, y, z = map(int, input().split()) # zいらなくない？仕様？
    unite(x, y)

# 一応全部findしてパス圧縮しとく、意味あるかは微妙w
for i in range(1, n + 1):
    find(i)

# グループ数数える(根の種類の数)
roots = set()
for i in range(1, n + 1):
    roots.add(parent[i])
print(len(roots))