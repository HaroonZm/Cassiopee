import sys
import bisect

input = sys.stdin.readline

N, M = map(int, input().split())
pictures = [tuple(map(int, input().split())) for _ in range(N)]
frames = [int(input()) for _ in range(M)]

# 額縁の大きさをソートしておく
frames.sort()

# 絵を価値の昇順、価値が同じなら大きさの昇順にソート
pictures.sort(key=lambda x: (x[1], x[0]))

used = [False]*M  # 額縁使用済み管理
count = 0

for s, v in pictures:
    # 大きさがs以下の額縁のうちで一番小さいものを探す
    idx = bisect.bisect_left(frames, s)
    # idxはs以上の額縁の位置なので、s以下の額縁はidxかその前
    # よってidx-1から開始し0方向に空いてる額縁を探す
    i = idx-1
    while i >= 0:
        if not used[i] and frames[i] >= s:
            used[i] = True
            count += 1
            break
        i -= 1

print(count)