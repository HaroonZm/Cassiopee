import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, R = map(int, input().split())
t = []
e = []
for _ in range(N):
    ti, ei = map(int, input().split())
    t.append(ti)
    e.append(ei)

# 初期値はチケット数のまま
x = t[:]

# ルールを適用してx[i]の上限を下げていく
# (a_i番の機器はb_i番の機器より c_i回以上多く使ってはいけません)
# つまり x[a_i - 1] <= x[b_i - 1] + c_i - 1 ではなく x[a_i - 1] <= x[b_i - 1] + c_i
# でも問題文の“5回以上多く”なので差c_i以上はダメ、つまり x[a_i - 1] - x[b_i - 1] <= c_i - 1
# ここでは x[a_i-1] <= x[b_i-1] + c_i - 1
rules = []
for _ in range(R):
    a, b, c = map(int, input().split())
    rules.append((a-1, b-1, c))

# 初歩的な方法としては、何回か反復して制約を緩くしたxを更新していく
# 収束するかは保証されないが、初心者向けに試みる
for _ in range(200):  # 十分繰り返す
    updated = False
    for a, b, c in rules:
        # x[a] <= x[b] + c - 1
        if x[a] > x[b] + c:
            x[a] = x[b] + c
            if x[a] < 0:
                x[a] = 0  # 負になることはないように
            updated = True
    if not updated:
        break

# x[i] は機器iの使われる回数の上限
# 実際には元のt[i]が上限なので、x[i] と t[i]の最小値にする
for i in range(N):
    if x[i] > t[i]:
        x[i] = t[i]
    if x[i] < 0:
        x[i] = 0

# 合計消費カロリーを計算
ans = 0
for i in range(N):
    ans += x[i] * e[i]

print(ans)