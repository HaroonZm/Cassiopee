# 問題の理解とアプローチ：
# M（2 ≤ M ≤ N）について、M の約数のうち M を除いたものの総積が M の 2 倍以上になるかどうかを判定する。
# M の約数を d_1, d_2, ..., d_k とし、その中の最大の約数は M 自身。
# M を除いた約数の積を P とする。
# 条件: P >= 2 * M
#
# 約数の積の性質：
# 約数が d_1, d_2, ..., d_k なら、約数の積は M^{k/2}（約数の個数 k が奇数なら平方根を考慮するが奇数個の場合も扱う）
#
# 条件式は次のように変形できる：
# P = M^{k/2 - 1} >= 2
# => M^{(k/2) -1} >= 2
# => (k/2) -1 >= log_M (2)
# => k/2 >= 1 + log_M(2)
# => k >= 2 + 2*log_M(2)
#
# 約数の個数 k を調べ、k が十分大きければ条件を満たす。
#
# 実際には M の約数の個数 d(M) を計算し、
# P = M^{(d(M) -1)/2} >= 2M
# 上記の不等式を確認し判定する。
#
# Mとd(M)から条件判定。
#
# 制約：
# Q, N 最大10^5なので事前に 1～10^5 の約数の個数と判定結果を計算し、
# クエリを高速に処理する。

import sys
import math

input = sys.stdin.readline

MAX = 10**5

# 約数の個数を求める配列
div_count = [0]*(MAX+1)

# エラトステネスの要領で約数の個数を記録
for i in range(1, MAX+1):
    for j in range(i, MAX+1, i):
        div_count[j] += 1

# 条件判定の事前計算結果を格納
# 条件： M^{(d(M)-1)/2} >= 2*M
# 両辺を M で割って： M^{(d(M)-1)/2 -1} >= 2
# 指数は (d(M)-1)/2 -1 = (d(M)-3)/2 なので、
# M^{(d(M)-3)/2} >= 2 となる
# M >= 2 なので Mの対数を使って判定するのが高速
# log_M(2) <= (d(M)-3)/2 になるかどうか

# 計算を対数に変換（底は e）
# 左辺の指数をかけて、(d(M)-3)/2 * log(M) >= log(2)
# これを満たす場合条件クリア

LOG2 = math.log(2)

answer = [0]*(MAX+1)
count_cum = 0
for M in range(2, MAX+1):
    d = div_count[M]
    exponent = (d - 3)/2
    if exponent < 0:
        # 指数が負なら M^{負数} < 1 < 2 なので条件不可
        satisfy = False
    else:
        lhs = exponent * math.log(M)
        satisfy = (lhs >= LOG2)
    if satisfy:
        count_cum += 1
    answer[M] = count_cum

Q = int(input())
for _ in range(Q):
    N = int(input())
    # 条件を満たす M の数は answer[N]
    print(answer[N])