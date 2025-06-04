import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 問題の操作を効率的に行うために、順列を環状リストとして扱う着想を用いる。
# 通常のリスト操作で部分列を切り出して移動すると時間超過（O(NQ)）となるため、
# 順列を循環的に見て、先頭の位置を更新するだけの方法に変換する。

N, Q = map(int, input().split())
a = list(map(int, input().split()))
queries = list(map(int, input().split()))

# aは1-based indexの値を含む順列なので、
# 各値の位置を高速に検索できるようindex_of_valを作成。
index_of_val = [0]*(N+1)
for i, val in enumerate(a):
    index_of_val[val] = i

# 以下のkeyアイデア：
# 順列を環状配列として扱い、現在の先頭のインデックスを管理する。
# クエリq_iの操作は、
# 　・q_iの位置j（0-based）を見つける。
# 　・a[j]をピボットにして L,Rを分割。
# 　・順列を R + q_i + L にする操作は、
# 　　環状配列の先頭を q_iのすぐ右の位置(j+1)に移動することと等価。
# よって、各クエリ時に先頭のインデックスを j+1 に更新すればよい。

head = 0  # 現在の先頭のインデックス（0-based）

for q in queries:
    pos = index_of_val[q]  # 元のaにおける位置
    # 現在のheadからの相対位置を考慮してposを計算しなおす必要がある。
    # 実は、index_of_valは元のaの位置のため、headのずれを補正する必要がある。

    # 実際の現在の位置は ((pos - head) mod N)
    # そこではない。逆にクエリ値qはvalueなので元の位置posは元のa内での位置。
    # 頭をheadに動かしているが、index_of_valは元のa上の位置。
    # 頭を動かしても各値のindex_of_valは変化しないのでposは変わらず良い。
    # メインの更新はhead=(pos+1) mod N にすれば良い

    head = (pos + 1) % N

# 最終結果はaのheadから始まるN個分の環状配列として出力すれば良い
res = []
for i in range(N):
    res.append(a[(head + i) % N])

print(' '.join(map(str, res)))