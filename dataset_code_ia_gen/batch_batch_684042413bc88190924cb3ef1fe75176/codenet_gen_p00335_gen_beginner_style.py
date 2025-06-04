N = int(input())
p = list(map(int, input().split()))

# 初期化: 各パンケーキの裏返し回数を0にする
flips = [0] * N

# まったく必要ない場合は0を出力
if sum(p) == 0:
    print(0)
    exit()

total = 0

# シンプルに左端から順に処理する
for i in range(N):
    need = p[i] - flips[i]
    if need <= 0:
        continue
    # 左端の場合は1枚だけ裏返すこともできる
    if i == 0:
        # 1枚だけ裏返す操作を need 回行う
        flips[i] += need
        total += need
    # 右端の場合は1枚だけまたは隣と2枚の操作ができるが基本は2枚ずつ
    elif i == N-1:
        # 1枚だけ裏返す操作を need 回行う
        flips[i] += need
        total += need
    else:
        # 中央は2枚一緒に裏返す必要がある
        # i番目とi+1番目のパンケーキを need 回裏返す
        # 位置は変わらないのでi+1も増える
        flips[i] += need
        flips[i+1] += need
        total += need * 2

print(total)