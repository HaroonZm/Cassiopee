# 入力される複数のデータセットに対し、
# a, b, c, d が 0〜1000 の範囲で a+b+c+d = n を満たす組み合わせの数を求める。
# n は最大4000。

# アプローチ:
# a,b,c,d の範囲は0〜1000なのでそれぞれ1001通りの値を取る。
# n の最大は4000。
# (a,b)の和を x = a+b とすると、x の範囲は0〜2000（0+0〜1000+1000）。
# 同様に (c,d) の和も y = c+d で 0〜2000。
# したがって、問題は x + y = n を満たす (x,y) の組み合わせ数を求めることに置き換えられる。

# 手順:
# 1. sums_ab[x]: a,bの組み合わせで和が x となる組み合わせ数を計算（0<=x<=2000）。
# 2. sums_cd[y]: 同様に c,d の組み合わせ数を計算。
# 3. n を入力されたとき、n <= 4000 なので
#    - x を 0〜min(n,2000) として、
#      sums_ab[x] * sums_cd[n-x] の和をとる。
# これが求める組み合わせ数。

# sums_ab と sums_cd は同じため一度だけ計算すればよい。

import sys

# a,b,c,d は範囲0～1000なので和は0～2000
MAX_SUM = 2000
MAX_VAL = 1000

# sums_ab[x] は a,bの組み合わせで和xとなる数
sums_ab = [0] * (MAX_SUM+1)

# a,bの全組み合わせで和をカウントする
for a in range(MAX_VAL+1):
    for b in range(MAX_VAL+1):
        sums_ab[a+b] += 1

# 以降は入力を読み込み、指定された n に対して結果を計算して出力

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    # nは最大4000、和の範囲0〜2000なので
    # xの範囲は0〜min(n,2000)
    count = 0
    start_x = max(0, n - MAX_SUM)  # n - 2000 以上でなければ sums_cd[n-x] は0
    end_x = min(n, MAX_SUM)
    for x in range(start_x, end_x+1):
        y = n - x
        count += sums_ab[x] * sums_ab[y]  # sums_cd = sums_abなので同じものを利用
    print(count)