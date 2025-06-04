N = int(input())
L = [int(input()) for _ in range(N)]

# Lの累積和を求める
prefix_sum = [0]
for length in L:
    prefix_sum.append(prefix_sum[-1] + length)

total_length = prefix_sum[-1]
answer = float('inf')

# 切れ目は1〜N-1までの位置にある
# 1箇所以上を切らないといけないため、少なくとも1回切る

# Nは最大50なので部分集合を全探索するのは2^(N-1)と大きいが、
# N=50でも2^49は大きい。だが制約が小さいのでbit全探索を試みる。

# 1〜N-1 の位置の切れ目から選択する部分集合をビットマスクで表す
for bit in range(1, 1 << (N-1)):
    pieces = []
    prev = 0
    # bitの立っているビットの位置を切れ目として使う
    for i in range(N-1):
        if bit & (1 << i):
            pieces.append(prefix_sum[i+1] - prev)
            prev = prefix_sum[i+1]
    pieces.append(total_length - prev)

    diff = max(pieces) - min(pieces)
    if diff < answer:
        answer = diff

print(answer)