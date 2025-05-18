# 数え上げで制約が 2 乗っぽいのでどうせ dp だろという気持ちになる
# なんで入力が数字で与えられるのかを考えるとちょっと視界が開ける

# よく考えると、できる列の制約は
# 「赤い/青いボールはできる列の i 個目までに A[i]/B[i] 個使える」
# と表せることがわかる
# これに気付けばあとは
#     dp[i][j] := i 個目まで並べたとき赤いボールを j 個使う場合の数
# とした dp が自然と思いつく

from itertools import accumulate
import numpy as np

def main():
    mod = 998244353
    B = list(map(int, input()))
    N = len(B)
    A = [2-b for b in B] + [0]*N
    B += [0] * N
    a = b = 0
    for i in range(2*N):
        b += B[i]
        if b > 0:
            b -= 1
            B[i] = 1
        a += A[i]
        if a > 0:
            a -= 1
            A[i] = 1

    A = list(accumulate(A))
    B = list(accumulate(B))

    dp = np.zeros((2*N+1, 2*N+1), dtype=np.int64)
    dp[0, 0] = 1
    for i, (a, b) in enumerate(zip(A, B), 1):
        dp[i, :] = dp[i-1, :]
        dp[i, 1:] = (dp[i, 1:] + dp[i-1, :-1]) % mod
        dp[i, :i-b] = 0
        dp[i, a+1:] = 0

    print(dp[2*N].sum() % mod)

main()