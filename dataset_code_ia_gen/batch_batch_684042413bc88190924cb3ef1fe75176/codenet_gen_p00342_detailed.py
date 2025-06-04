# 解法の説明:
# 問題は、異なるN個の自然数から4つを選び、それらをA,B,C,Dとしたとき (A + B) / (C - D) の最大値を求めること。
# 条件はN≥4、値は全て異なる自然数。

# 重要なポイント:
# - C-Dはゼロであってはならず、分母として使用できない。
# - Nが最大1000で、4重ループは計算量的に厳しい。
# - よって、効率的に計算を行う必要がある。

# アプローチ:
# 1. 分子はA + Bの組み合わせ。A,Bは異なる2個の数。
# 2. 分母はC - D。C,Dも異なる2個の数でC≠D。
# 3. 4つの数は全て異なる必要がある。

# 具体的な解法:
# - 全てのペアの和をリスト化し、 (sum, a, b) を記録。ペアの個数は最大 約500,000。
# - 全てのペアの差をリスト化し、 (diff, c, d) を記録。差は正負両方で記録し、diff≠0のみ保存。ペア数も約500,000。
# - 和のペアと差のペアを全探索し、4つの番号が重複しない組み合わせの中で (sum)/(diff) の最大値を計算。
# - ただし全探索（5e5 * 5e5 = 2.5e11）は無理なので、工夫が必要。

# 工夫:
# - 差のペアを辞書にまとめ、key: 差, value: list of (c,d)
# - 和のペアを大きい順にソートし、差のペアを小さい絶対値順に探索。
# - 大きい和と小さい差が最大値を作りやすい。
# - 差のペアは0に非常に近い差は除外しても良いが制約に注意。

# しかし無理なため以下の近似戦略をとる:
# - 上位K (例: 500)の和ペアと上位K(例: 500)の差ペアのみを探索する（和は大きい順, 差は絶対値小さい順） 
# - K=500だと約25万の組み合わせなので十分高速。

# 最終的に最大値を求め、誤差10^-5以内で出力。

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 全ペアの和を作成 (sum, idx1, idx2)
sums = []
for i in range(N):
    for j in range(i+1, N):
        sums.append((A[i] + A[j], i, j))
# 和は大きい順にソート
sums.sort(key=lambda x: x[0], reverse=True)

# 全ペアの差を作成 (diff, idx1, idx2)
diffs = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        diff = A[i] - A[j]
        if diff != 0:
            diffs.append((diff, i, j))
# 差を絶対値の小さい順にソート（分母が小さいほうが結果が大きくなる可能性がある）
diffs.sort(key=lambda x: abs(x[0]))

# 探索範囲を制限（パフォーマンス確保のため）
K = 500  # 500に設定、適宜調整可能

max_value = -float('inf')

for si in range(min(K, len(sums))):
    s_val, s_i1, s_i2 = sums[si]
    for di in range(min(K, len(diffs))):
        d_val, d_i1, d_i2 = diffs[di]

        # ４つとも異なるか確認
        indices = {s_i1, s_i2, d_i1, d_i2}
        if len(indices) < 4:
            continue

        val = s_val / d_val
        if val > max_value:
            max_value = val

# 出力。誤差10^-5は%.5fで対応
print(f"{max_value:.5f}")