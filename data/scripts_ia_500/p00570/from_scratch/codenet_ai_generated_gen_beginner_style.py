N, K = map(int, input().split())
T = [int(input()) for _ in range(N)]

# 訪問者ごとにストーブをつけると、合計の点火回数はN回になる
# 点火回数をK回に減らすために、連続した滞在区間の間の空白時間を隙間としてつなげることができる
# 空白時間のリストを作り、それを小さい順にK-1回分だけ減らす

intervals = []
for i in range(N):
    intervals.append((T[i], T[i] + 1))

total = intervals[-1][1] - intervals[0][0]  # すべて繋げたときの時間

gaps = []
for i in range(N - 1):
    gap = intervals[i + 1][0] - intervals[i][1]
    gaps.append(gap)

gaps.sort(reverse=True)

for i in range(K - 1):
    if i < len(gaps):
        total -= gaps[i]

print(total)