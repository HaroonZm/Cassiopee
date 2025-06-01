import sys
input=sys.stdin.readline

N,C=map(int,input().split())
INF=10**15

# 頂点は0～N-1 (学生番号 1～N を 0～N-1 に)
# d[i] は 学生iの位置（先頭からの距離）
# 制約を距離差に変換して辺を張る
# 順序制約と距離制約を合わせて不等式として扱う

edges=[]

# 人1(番号0)の位置は0に固定: d[0]=0
# -> d[0]<=0, 0<=d[0]
# これに対応するために、追加頂点として番号Nを導入し、d[N]=0とする方法もあるが
# ここでは d[0]=0 に固定し、それを基準として他の値を推定

for _ in range(C):
    line=input().rstrip()
    # 形式: aioibisd
    # ai: 数字 (1～N) o_i: <=,>=,* s_i: +,- d_i: 数字
    # 例: 1<=2-1
    # 分割
    # aとbを抽出
    # oの場所探索 (<=, >=, *)
    if '<=' in line:
        idx=line.index('<=')
        a=int(line[:idx])
        o='<=', 
        b_s=line[idx+2:]
    elif '>=' in line:
        idx=line.index('>=')
        a=int(line[:idx])
        o='>=',
        b_s=line[idx+2:]
    else:
        idx=line.index('*')
        a=int(line[:idx])
        o='*',
        b_s=line[idx+1:]
    b=int('')
    # b_s は b s d の組み合わせ
    # sは + or -
    # dは数値
    # b_sの先頭の数字抽出
    i1=0
    while i1<len(b_s) and b_s[i1].isdigit():
        i1+=1
    b=int(b_s[:i1])
    s=b_s[i1]
    d=int(b_s[i1+1:])

    # 順序制約を距離差に変換
    # d[a-1], d[b-1] を使う

    if o[0]=='<=':
        # a は b より先または同じ位置
        # d[a-1]<=d[b-1]
        # d[a-1] - d[b-1] <= 0
        edges.append( (b-1,a-1,0) ) # d[a-1]<=d[b-1]→ d[b-1] - d[a-1]>=0 → (a-1)->(b-1) に重み0は方向逆なので (b-1)->(a-1) に0辺を張る(これはd[b]<=d[a]+0の形)
        # 実はベルマンフォードで d[v]<=d[u]+w μορφに直すため、d[a]<=d[b]+0なので辺は (b)->(a) w=0
    elif o[0]=='>=':
        # a は b より後または同じ位置
        # d[a-1]>=d[b-1]
        # d[b-1]-d[a-1]<=0
        # d[a-1]<=d[b-1]+0
        edges.append( (a-1,b-1,0)) # (b)->(a) w=0と等価だがbとaが逆, d[a]<=d[b]+0なので辺は(b)->(a) なので (b-1)->(a-1) w=0
        # 上は矛盾？よく確認: d[a]>=d[b]⇒ d[b]-d[a]<=0 ⇒ d[a]<=d[b]+0 ⇒ 辺 (b)->(a) w=0
    else:
        # * は順序制約なし
        pass

    # 距離制約を距離差に変換
    # a,b間距離 |d[a-1]-d[b-1]| >= d か <= d

    if s=='+':
        # aとbはdメートル以上離れる
        # |d[a]-d[b]| >= d
        # → d[a]-d[b]>=d または d[b]-d[a]>=d
        # これは距離の不等式のうちどちらかを選べるわけではなく、両方とも満たすことは不可能なので
        # しかし行列は1次元なので、どちらか満たせばよい
        # 制約を満たす配置が存在するかどうかは探索が必要
        # この問題の設計より、両方の条件を分割して距離差制約を2辺で追加し、
        # 片方ずつ考慮した形に変換する
        # 距離差≥dは不等式に変換不能(d[v]−d[u]>=dは d[u]-d[v]≤-d として考える)
        # 逆向き辺を張る

        # d[a] - d[b] >= d : d[b] - d[a] ≤ -d
        edges.append( (a-1,b-1,-d) )
        # d[b] - d[a] >= d : d[a] - d[b] ≤ -d
        edges.append( (b-1,a-1,-d) )
    else:
        # s=='-'
        # aとbはdメートル以内に並ばなければならない
        # |d[a]-d[b]| <= d
        # → d[a]-d[b] <= d and d[b]-d[a]<=d
        edges.append( (b-1,a-1,d) )
        edges.append( (a-1,b-1,d) )

# d[0]=0 に固定するために頂点Nを追加し、d[N]=0
# そして (N) -> (0) 辺0, (0)->(N) 辺0を追加し固定
for i in range(N):
    edges.append( (N,i,INF) ) # 余分な辺をいれておくが
edges.append( (N,0,0) )
edges.append( (0,N,0) )

V=N+1

dist=[INF]*(V)
dist[N]=0

# ベルマンフォードで最長路問題（制約が d[v] <= d[u] + w の形なので）
# ただし、この形の重みを利用して長さの最大値を求めるには辺重みの逆符号化や負閉路検出を行う
# ここでは d[v] <= d[u]+w の制約を使い dist[v]=min(dist[v],dist[u]+w)

for _ in range(V):
    update=False
    for u,v,w in edges:
        if dist[u]==INF:
            continue
        nd=dist[u]+w
        if nd<dist[v]:
            dist[v]=nd
            update=True
    if not update:
        break
else:
    # N回反復しても収束しなければ負閉路がある = 矛盾(不可能)
    print(-1)
    sys.exit()

# 定義よりd[N] = 0、d[0]=? は
# 問題は距離が最大になる並べ方を求める
# dist[i] は頂点Nからの最短距離であり、d[i] <= dist[i] + 定数で表現される
# 今は dist[i] は最小値であり、0が基点なので d[i] = dist[i]

# 最大距離 = max(d[i]) - min(d[i]) だが d[0]は0固定している ?
# 今の設定では d[0]は固定していないので dist[0]が位置

# ただし dist[]は最小値なので 最大距離は最大の dist[i] - dist[0]

min_pos=dist[0]
max_pos=max(dist[:N])

if max_pos - min_pos > INF//2:
    print('inf')
    sys.exit()

# 先頭は常に番号1の人がいる→d[0]=0に固定
# dist[0]の値は0以上かもしれない？実はdist[N]=0基準なので dist[0]は0以下かも

# 先頭固定のため dist[i] - dist[0] に変換すればよい
max_dist=max_pos - dist[0]

print(max_dist)