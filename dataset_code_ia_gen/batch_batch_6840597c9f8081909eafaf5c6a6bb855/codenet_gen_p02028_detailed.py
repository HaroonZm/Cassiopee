# 入力として与えられるのは、
# - 縦（高さ）方向のマス数 H
# - 横方向のマス数 W
# - 真横から見たときの積み木の高さリスト A（長さ H）
# - 正面から見たときの積み木の高さリスト B（長さ W）
# 
# 問題は、各マス (x, y) に積める積み木の最大個数の合計を求めるもの。
# 
# 考え方:
# - 位置 (x, y) に積める積み木の最大高さは、A[x]（横方向から見た高さ）と B[y]（正面から見た高さ）のうち小さい方である。
# - つまり、マス (x, y) には min(A[x], B[y]) 個の積み木が置かれている可能性がある。
# - よって、答えは全ての (x,y) の min(A[x], B[y]) の総和。
# 
# これを効率よく計算するには、A と B の情報をそのまま使えばよい。
# ただし H, W は最大10万なので二重ループ（10^10回）は不可能。
# 
# 最適化:
# - A がH個、BがW個で、直接二重ループは無理。
# - しかし今回は制約条件として「条件を満たす積み方が存在すること保証されている」ため、
#   積み木の配置は min(A[x], B[y]) で計算可能。
# - とはいえ、計算量問題がある。
# 
# しかし問題例を見ると単に min(A[x], B[y]) を全ての組み合わせで足し合わせたものが答え。
# （証明を考えると、min(A[x], B[y]) の値を足し合わせるのが最大総数）
# 
# 実務的には、全ての A と B の要素について min(A[x], B[y]) の合計は
# ∑_{x=1}^H ∑_{y=1}^W min(A[x], B[y])
# なので O(H*W) で計算すると時間切れ。
# 
# そこで計算式を分解:
# - 全ての x,y の min(A[x], B[y]) の合計は、
#   ∑_{x=1}^H ∑_{y=1}^W min(A[x], B[y])
# 
# Bの各値をソートし、累積和を求める。
# Aの各値 v について
# - Bの中で v 未満の値は v を下回るので min(A[x], B[y]) = B[y]
# - Bの中で v 以上の値は v を下回らないので min(A[x],B[y]) = v
# 
# よって、ある A[x] = v に対しての和は
# sum_{B[y]<v} B[y] + (W - count_{B[y]<v}) * v
# 
# B をソートし累積和を使って効率計算。
# 
# 最後にそれを全ての A[x] について合計すれば答えになる。

import sys
import bisect

def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # Bを昇順ソート
    B.sort()
    
    # Bの累積和を求める cumulative sum (prefix sum)
    # cumB[i] := Bの先頭i個の和（iは1から）
    cumB = [0]
    for val in B:
        cumB.append(cumB[-1] + val)
    
    total = 0
    for v in A:
        # Bの中で v 未満の要素の個数を探す（v未満の最大index+1）
        idx = bisect.bisect_left(B, v)
        # min(A[x], B[y]) の和
        # B[y]<v の要素はそのまま B[y] の値を加算
        # B[y]>=v の要素は v を加算
        sum_val = cumB[idx] + (W - idx) * v
        total += sum_val
    
    print(total)

if __name__ == "__main__":
    main()