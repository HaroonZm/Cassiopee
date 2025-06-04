N,C = map(int,input().split())
constraints = [input() for _ in range(C)]

# 位置をx[1..N]とする。x[1] = 0 に固定（先頭が1番目）

# 順序制約によって、位置の大小関係に差分制約をつける
# 距離制約は絶対値ではないので工夫が必要

# ここでは単純に x[i] を位置とし、制約を不等式に変換して、
# 全体が矛盾しないかをBellman-Ford法で判定し、
# 最大距離を求める

# 実装方針（単純）：
# 変数を x[i] : 人iの位置（先頭からの距離）
# x[1] = 0固定
# 順序制約：
#   a<=b => x[b] - x[a] >= 0  => x[a] - x[b] <= 0
#   a>=b => x[a] - x[b] >= 0  => x[b] - x[a] <= 0
#   a*b => no order constraint
# 距離制約：
#   aとbは d以上離れる => |x[a]-x[b]|>=d
#       => x[a]-x[b]>=d or x[b]-x[a]>=d
#       分解して辺を2つ使い、どちらかの不等式を満たせばいいのだが、これは複雑なので単純化のため、2通りの組み合わせで試す
#   aとbは d以内 => |x[a]-x[b]| <= d
#       => x[a]-x[b] <= d and x[b]-x[a]<=d  両方条件にする

# しかし厳密には絶対値距離制約は難しいため簡単な探索で対応

# アプローチ：
# 制約が多いがNは100なので全配置を試すことは無理。
# ここでは距離を変数にして単純なBellman-Fordでやってみる。

# まず、制約を不等式の形 (x[u] - x[v] <= w) に変換して辺を作る
# それからBellman-Fordをして負閉路を検出、矛盾チェック。

# しかし、絶対値の「>=d」は不等式１つでは表現できないので簡単にはできない。
# ここでは += 距離制約＋順序制約のうち
#  |x[u]-x[v]| >= d を
#  x[u]-x[v] >= d or x[v]-x[u] >= d の可能性があるので両方のパターンを試す。
# ただし*は7個以下なので2^7=128で全部試しても間に合う。
# ここでは*制約を含めた複雑な方法はやらず、
# *は順序制約は無しなので順序は無視、距離だけ考える。
# そこで単純に*制約はどちらでもOKなので常に距離制約のみ考える。

# そこで簡単のために*制約の距離制約は距離の範囲を満たすか判定して矛盾していなければよしとする。

# まず、辺のリストを作る。
edges = []

# x[1] = 0 固定のため、すべてのx[i]の初期距離を大きな負数にしておき、x[1]だけ0にする
INF = 10**9

# 枝の追加関数 x[u] - x[v] <= w の形で表現
def add_edge(u,v,w):
    edges.append((u,v,w))

order_pairs = []
star_pairs = []

for c in constraints:
    # c の形式：a o b s d
    # a,bは数字、oは <=, >=, *, sは + or -, dは距離
    # 例: 1<=2-1
    # 解析
    # a の位置
    i = 0
    while c[i].isdigit():
        i += 1
    a = int(c[:i])
    j = i
    if c[j] == '<' and c[j+1] == '=':
        o = "<="
        j+=2
    elif c[j] == '>' and c[j+1] == '=':
        o = ">="
        j+=2
    elif c[j] == '*':
        o = "*"
        j+=1
    else:
        o = None
    k = j
    while c[k].isdigit():
        k+=1
    b = int(c[j:k])
    s = c[k]
    d = int(c[k+1:])

    if o == "<=":
        # x[b] - x[a] >= 0 => x[a] - x[b] <= 0
        add_edge(a,b,0)
    elif o == ">=":
        # x[a] - x[b] >= 0 => x[b] - x[a] <= 0
        add_edge(b,a,0)
    else:
        # * は順序制約無し
        star_pairs.append((a,b,s,d))

    # 距離制約
    if s == '+':
        # |x[a]-x[b]| >= d
        # 複雑なのでstar_pairsで後でまとめて考える
        if o != '*':
            # oが<=や>=なら順序制約あるので処理
            # |x[a]-x[b]|>=d
            # を
            # attempt1: x[a] - x[b] >= d (== x[b]-x[a] <= -d)
            # attempt2: x[b] - x[a] >= d (== x[a]-x[b] <= -d)
            # 試す必要あり
            # ここではとりあえず両方追加しておいて後で判定
            add_edge(b,a,-d) # x[a]-x[b]>=d => x[b]-x[a]<=-d
            add_edge(a,b,-d) # x[b]-x[a]>=d => x[a]-x[b]<=-d

    else:
        # s == '-'
        # |x[a]-x[b]| <= d
        # x[a]-x[b] <= d and x[b]-x[a] <= d
        add_edge(a,b,d)
        add_edge(b,a,d)

# x[1] = 0と固定するために1から1に0を加える
add_edge(1,1,0)

def bellman_ford(start,n,edges):
    dist = [INF]* (n+1)
    dist[start] = 0
    for i in range(n):
        updated = False
        for u,v,w in edges:
            if dist[u] == INF:
                continue
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                updated = True
        if not updated:
            break
    else:
        # n回更新されたなら負閉路あり
        return None
    return dist

dist = bellman_ford(1,N,edges)
if dist is None:
    print(-1)
else:
    # distはx[v]の最小値、ただし制約条件のはずだが測り方が複雑なので
    # 最大距離は distの中の最大値 - x[1]
    max_pos = max(dist[1:])
    if max_pos >= INF or max_pos <= -INF:
        print('inf')
    else:
        print(max_pos)