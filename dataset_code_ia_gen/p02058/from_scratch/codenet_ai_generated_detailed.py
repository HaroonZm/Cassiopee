import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

# 問題:
# N頂点の木において、
# K個の空でない連結部分グラフの組で、
# 互いに頂点が重ならないものの個数を求める。
# 順序は考えず、組み合わせとして数える。

# アプローチ概要:
# - 木において連結部分グラフは、頂点集合が部分木の形になる。
# - 部分グラフが連結 ⇒ 部分木に相当。
# - 頂点集合が重ならないK個の連結部分木の組の数を求める。
#
# DPの設計:
# - 木DPで根から下に向かって考える。
# - 各頂点uに対してf[u][k][used]: uの部分木内で、
#   使用済みか否か(used=0 or 1),
#   選んだ連結部分グラフの数がk個である場合の数を管理する。
#
#   used=0: u自身は部分グラフに含まれていない
#   used=1: u自身は部分グラフに含まれている（かつ根の連結成分の一部）
#
# - 子の情報をマージする際に、usedの状態で場合分けして結合。
#
# - 最終的に根のf[root][K][0]+f[root][K][1]が答え。
#
# 計算量:
# - 各頂点でのDPはO(K^2)
# - N=1e5, K=300 は工夫が必要だが高速化を施せば可能。
#
# 注意:
# - 頂点番号は1からN。
# - 結果をMODで割った余りを出力。

N, K = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

# DP配列のMAXはK+1で1ベース
# f[u][k][used] = 数
# used=0 or 1
# 子DPのために遅延で計算
def mod_add(a,b):
    a += b
    if a >= MOD:
        a -= MOD
    return a

def mod_mul(a,b):
    return (a*b) % MOD

from collections import deque

sys.setrecursionlimit(10**7)
visited = [False]*(N+1)

def dfs(u):
    visited[u] = True
    # f[u][k][used]: uの部分木でk個の連結部分グラフを作る場合の数
    # used=0 uは部分グラフに含まない
    # used=1 uが部分グラフに含まれている（uを含む連結成分に属する）
    f0 = [0]*(K+1)
    f1 = [0]*(K+1)

    # ベースケース
    # uを部分グラフに含まない場合は部分グラフ数0通りは1通り（空集合）だが
    # 空集合はだめなのでk=0は0通りにする。使わないが念のため。
    # uを部分グラフに含む場合は1個の連結部分グラフを単独で作る -> k=1通り1
    f0[0] = 1  # 空集合的意味合い。ここで空集合は使わないが計算用に残す。
    f1[1] = 1

    for w in edges[u]:
        if visited[w]:
            continue
        dfs(w)

        # 子wで計算したf0w,f1wを取得
        f0w = dp0[w]
        f1w = dp1[w]

        # マージ用配列初期化
        nf0 = [0]*(K+1)
        nf1 = [0]*(K+1)

        # 状態遷移
        # uの状態 used=0の場合:
        #  - 子は部分グラフに含めなくても良い => 子はused=0 or 1のどちらでもいい
        #  - k個の部分グラフはuの部分木全体のk個の部分グラフの総数
        #  - u自体は含まないのでkは子の合計
        #
        # uの状態 used=1の場合:
        #  - uと連結する部分グラフのうち、uを含んでいる成分に子のどの成分を追加するか考える
        #  - 子wがused=1なら、uの成分に繋がるためk数は増えない（結合）
        #  - 子wがused=0なら、子の部分グラフはuの成分と分かれて別にあるのでkは子の分だけ増える
        #
        # 具体的な遷移:
        # k1=かつうの現在のk個の部分グラフ数
        # k2=子のk個の部分グラフ数

        for k1 in range(K+1):
            if f0[k1]==0 and f1[k1]==0:
                continue
            for k2 in range(K+1):
                if f0w[k2]==0 and f1w[k2]==0:
                    continue
                # used=0時の更新
                # u not included:
                # 子wはused=0 or 1のどちらでもよいが部分グラフ数の合計はk1+k2
                nk = k1 + k2
                if nk <= K:
                    val = f0[k1] * (f0w[k2] + f1w[k2]) % MOD
                    nf0[nk] = (nf0[nk] + val) % MOD

                # used=1時の更新
                # u included: uの成分にwのused=1を結合 → 部分グラフ数の合計は k1 + k2 - 1
                # もしくはwのused=0は別部分グラフ → 部分グラフ数の合計は k1 + k2
                # ここでk1はuの成分の個数, なのでk1,k2 >=1 (f1はk>=1)
                # f1[k1] * f1w[k2] -> k1+k2-1個
                if f1[k1] != 0 and k2 > 0:
                    nk = k1 + k2 - 1
                    if nk <= K:
                        val = f1[k1] * f1w[k2] % MOD
                        nf1[nk] = (nf1[nk] + val) % MOD
                # f1[k1] * f0w[k2] -> k1 + k2個
                if f1[k1] != 0 and f0w[k2] != 0:
                    nk = k1 + k2
                    if nk <= K:
                        val = f1[k1] * f0w[k2] % MOD
                        nf1[nk] = (nf1[nk] + val) % MOD

        f0 = nf0
        f1 = nf1

    dp0[u] = f0
    dp1[u] = f1

dp0 = [[0]*(K+1) for _ in range(N+1)]
dp1 = [[0]*(K+1) for _ in range(N+1)]
dfs(1)

# 答えはrootがused=0、used=1の両方でk=Kの和
ans = (dp0[1][K] + dp1[1][K]) % MOD
print(ans)