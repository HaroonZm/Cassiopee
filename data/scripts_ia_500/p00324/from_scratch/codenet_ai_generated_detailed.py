# N個の整数から、合計が0になる最長の連続部分配列の長さを求める問題です。
# アプローチは「累積和」と「ハッシュマップ」を使うことです。
#
# 1. 累積和を計算します。sum[i]を0からi-1までの和と定義します（sum[0] = 0）。
# 2. 2つの位置i, j (i < j)についてsum[j] - sum[i] = 0ならば、区間[i, j-1]の合計が0になります。
# 3. したがって、同じ累積和の値が現れた最初のインデックスと現在のインデックスの差がその0になる部分区間の長さになります。
# 4. ハッシュマップに最初に現れた累積和のインデックスを記録しておき、
#    同じ累積和が出るたびに最大区間長を更新します。

import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    arr = [int(input()) for _ in range(N)]

    prefix_sum = 0
    index_map = {0: 0}  # 累積和 -> 最初に出現したインデックス
    max_length = 0

    for i in range(1, N + 1):
        prefix_sum += arr[i - 1]
        if prefix_sum in index_map:
            # 以前に同じ累積和が現れた場合、その間の区間和は0
            length = i - index_map[prefix_sum]
            if length > max_length:
                max_length = length
        else:
            # 初めての累積和なら位置を記録
            index_map[prefix_sum] = i

    print(max_length)

if __name__ == "__main__":
    main()