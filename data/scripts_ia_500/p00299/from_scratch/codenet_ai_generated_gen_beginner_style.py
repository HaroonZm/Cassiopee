N,C = map(int, input().split())
constraints = [input() for _ in range(C)]

# 初期化
# pos[i]はi番目の人の位置を表す変数とする
# 頑張って次元をN+1にして1始まりにする
pos = [None]*(N+1)

# 順序制約を扱うために、N人の順序(位置)は整数の並びでなくても良いので、
# 順序制約を満たすように数値を割り当てつつ、不可能チェックを行う。
# また位置は距離なので0以上の実数を想定。最小距離は0。
# ここでは簡単に各学生の位置を表す変数を用意し、制約を不等式として扱う。

# グラフで不等式制約をBellman-Ford法で解くアプローチを使う。
# 頂点は学生番号(1～N)
# 辺は差分制約として表現
# pos[b] - pos[a] >= d なら辺(a,b) weight d
# 逆は辺(b,a) weight -d

edges = []

# 頭は1番目が先頭で位置0と固定する
# 位置は距離なので非負という明記はないが位置の基準を0とすることはOK
# pos[1] = 0 と固定 => pos[i] - pos[1] >= 0 => edge(1,i) weight 0も入れる
for i in range(2, N+1):
    edges.append( (1, i, 0) )  # pos[i] - pos[1] >= 0

import sys

INF = 10**15

# 位置は実数だが整数で扱う。Bellman-Fordで最長路(最大距離)問題になるので
# 使用する辺は不等式を変形し(pos[b] - pos[a] >= d なら pos[a] - pos[b] <= -d として負の重みの辺を使う)
# ここで最大距離を求めたいので、実は逆向きに考えて最大距離を求めるBellman-Fordをする。

# pos[i]の最小値をdist[i]として、dist[i]はpos[i]の最大値のマイナスに対応。
# つまり最大pos[i]を求めるために最小を変えて不等式を逆にする。
# これが複雑なので簡単にbellman-fordで負閉路チェックをして無限遠判定をしよう。

# 実装として、pos[i]の値をdist[i]とし、
# pos[b] >= pos[a] + d という不等式は
# dist[b] >= dist[a] + d なので、
# グラフの辺(a,b)に重みdを加え、dist[b]をdist[a] + d以上に更新する。

# これを行い負閉路なしで最大距離を求める。

def bellman_ford(n, edges, start):
    dist = [-INF]*(n+1)
    dist[start] = 0
    for i in range(n):
        updated = False
        for a,b,w in edges:
            if dist[a] == -INF:
                continue
            if dist[b] < dist[a] + w:
                dist[b] = dist[a] + w
                updated = True
        if not updated:
            break
        # n回目で更新されたら正の閉路（ここで正の閉路が意味するのは不可能ではなく、無限に距離を伸ばせる状態）
        if i == n-1 and updated:
            return None, True
    return dist, False


# 制約を辺に変換

# o_iについて
# <= : aはbより先か同じ位置 => pos[a] <= pos[b]
# これより pos[b] - pos[a] >= 0 より 辺(a,b,0)

# >= : aはbより後か同じ位置 => pos[a] >= pos[b]
# これより pos[a] - pos[b] >= 0 => 辺(b,a,0)

# * : 順序制約なし -> 放置

# s_iについて
# + : a,bはd以上離れる => |pos[a]-pos[b]| >= d
# d : d_iの値

# - : a,bはd以内に並ぶ => |pos[a]-pos[b]| <= d

# 与えられた制約は距離制約と順序制約の組み合わせ。

# 順序制約を得る辺の追加、
# 距離制約は二つの不等式に変換し、両方満たすように変換
# |pos[a]-pos[b]| >= d
# => pos[a] - pos[b] >= d or pos[b] - pos[a] >= d
# これは片方だけでなくどちらかが成り立てば良いが全体としては論理和なので単純な不等式では表せない。
# → なのでこの問題の制約は論理和になっている。
# だが順序制約で片方を限定しているから実質片方だけ見れば良い。

# 距離制約 |pos[a]-pos[b]| <= d は pos[a]-pos[b] <= d and pos[b]-pos[a] <= d の二つの不等式。

# で、順序制約ででa,bの位置関係が決まっている場合は距離制約の論理和は切り替える。

# aがbより先か同じなら pos[a] <= pos[b]
# なので pos[b]-pos[a] >= 0
# ここで「>= d」とか「<= d」を満たすか判断。

# まとめると以下のように単純化

for c in constraints:
    # cの形は a o b s d
    # a,b:番号 (1~N)
    # o: <=, >=, *
    # s: + or -
    # d:整数 >=0
    # 例: 1<=2-1  1<=2+5  2*3+1
    
    # 文字列パース
    # 例: '1<=2-1'
    # a:数字の先頭
    # o:2文字か1文字
    # b:数字
    # s:1文字
    # d:数字の終わりまで

    import re
    m = re.match(r"(\d+)(<=|>=|\*)(\d+)([+-])(\d+)", c)
    if not m:
        print(-1)
        exit()
    a = int(m.group(1))
    o = m.group(2)
    b = int(m.group(3))
    s = m.group(4)
    d_ = int(m.group(5))
    
    # 順序制約 != "*"ならば追加
    # pos[b]-pos[a]>=0 (a<=b)
    # or pos[a]-pos[b]>=0 (a>=b)
    # or 無し (*)
    if o == "<=":
        edges.append( (a,b,0) )
    elif o == ">=":
        edges.append( (b,a,0) )
    # ==*==の場合は何もしない
    # 次に距離制約 s,d_
    if s == "+":
        # pos[a]とpos[b]はd_以上離れる
        # |pos[a]-pos[b]| >= d_
        # => pos[a]-pos[b] >= d_ or pos[b]-pos[a] >= d_
        # つまり二つの不等式のどちらかを満たせば良い
        # 順序制約がある場合はどちらか選べる
        # ない場合( * )は両方の組み合わせを満たす並びを考えるのは難しい
        # ここでは単純に両方の不等式を考えて矛盾ないか見る
        
        # ただしoが '*'（順序なし）の場合は、
        # 最悪ダメな場合もある。とりあえず2つの辺をどちらも加えることで矛盾を検出できる
        
        edges.append( (a,b,d_) ) # pos[b] - pos[a] >= d_
        edges.append( (b,a,d_) ) # pos[a] - pos[b] >= d_
    else: # s == "-"
        # pos[a],pos[b]はd_以内
        # |pos[a]-pos[b]| <= d_ => 
        # pos[a]-pos[b] <= d_ and pos[b]-pos[a] <= d_
        # 両方を不等式にし直す
        # pos[a] <= pos[b] + d_ => pos[a] - pos[b] <= d_  => pos[b] - pos[a] >= -d_
        edges.append( (b,a,-d_) )
        # pos[b] <= pos[a] + d_ => pos[b] - pos[a] <= d_ => pos[a] - pos[b] >= -d_
        edges.append( (a,b,-d_) )

# pos[1] = 0
# pos[1]の値を0に固定し、dist[1] = 0とするのでこれを満たすようにする。

# Bellman-Fordでdist[i]はpos[i]の最大値とする
# 実装はdist[i]初期値 -INF, dist[1]=0
# edgesとして(a,b,w)は dist[b] >= dist[a] + wを表す

dist, has_pos_cycle = bellman_ford(N, edges, 1)

if dist is None and has_pos_cycle:
    # 無限に距離を伸ばせる(正閉路あり)
    print("inf")
    exit()

if dist is None:
    # 何かあったら不可能
    print(-1)
    exit()

# posはdistの最大値、dist[i]がpos[i]の最大値

# max position diff = max(dist) - dist[1]
maxd = max(dist[1:]) - dist[1]

# もしinf判定はしているが、制約がない場合のinfも考える
if C == 0:
    # 制約無しならどんどん離せるのでinf
    print("inf")
else:
    # 制約で距離を無限に伸ばせる場合は無限と判定済み
    # dist内に不可能な部分がなければ最大距離を出力
    # もしdistに-NINFがあったら不可能(未到達)
    if any(d == -INF for d in dist[1:]):
        print(-1)
    else:
        print(maxd)