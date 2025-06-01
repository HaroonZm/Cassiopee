# 入力例を読み取り、問題の設定を満たす給水容器の最小数を求めるプログラム

# 解法のポイント：
# - それぞれの部員は1単位時間の終わりに給水所に到着し、必ず中身入り容器を取る。
# - 次の到着では空の容器を置き中身入り容器を取る。この空の容器は1単位時間後に中身入りになる。
# - 複数の部員が同じ給水所に同時に着く場合もあるため、同一時刻・同一場所で必要な容器数をカウントする必要がある。
# - 部員は全員容器を持たずにスタートし、練習終了時のT単位時間の到達時点でも給水が必要。

# アプローチ：
# - 各部員のペースから、各時刻 t (1 <= t <= T)での走行距離を `pos = (p_i * t) % R` で求める。
# - (時刻 t, 給水所位置 pos) が必要となる容器数をカウント。
# - 最終的に全ての (t, pos)場面での最大容器数が答え。

N, R, T = map(int, input().split())
paces = [int(input()) for _ in range(N)]

# (時間, 位置)ペアでの必要容器数をカウント
from collections import defaultdict

# key: (time, position), value: 必要な容器数
water_counts = defaultdict(int)

for p in paces:
    for t in range(1, T+1):
        pos = (p * t) % R
        water_counts[(t, pos)] += 1

# 最大必要容器数を計算
answer = max(water_counts.values()) if water_counts else 0
print(answer)