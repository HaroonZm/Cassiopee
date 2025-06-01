n = int(input())
bulbs = list(map(int, input().split()))

def max_alternating_length(arr):
    max_len = 1
    length = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            length += 1
        else:
            max_len = max(max_len, length)
            length = 1
    max_len = max(max_len, length)
    return max_len

# まず機械を使わない場合の最大交互列長を求める
ans = max_alternating_length(bulbs)

# 機械は1回だけ使える。全ての区間[l,r]で反転させたときの交互列の長さを調べるのは無理なので、
# 初心者らしい簡単な方法として、全ての区間を試して反転してから交互列長を計算する方法をとる。
# 入力サイズが大きいが、ここでは簡単な実装を優先するため、全探索してみる。

for l in range(n):
    for r in range(l, n):
        flipped = bulbs[:]
        # 反転操作部分
        for i in range(l, r+1):
            flipped[i] = 1 - flipped[i]
        length = max_alternating_length(flipped)
        if length > ans:
            ans = length

print(ans)