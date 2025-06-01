N = int(input())
S = input()

MOD = 10007

members = ['J', 'O', 'I']

# 全ての参加パターン（0~7のビットで表現）
patterns = []
for bit in range(1, 8):  # 0は活動なしなので除く
    group = []
    for i in range(3):
        if bit & (1 << i):
            group.append(members[i])
    patterns.append((bit, group))

# 初日は責任者と鍵持ち(J)が参加しているパターンを探す
dp = [[0]*8 for _ in range(N)]
start_responsible = S[0]

# 鍵持ちは最初J君なのでbit 1<<0 = 1
for bit, group in patterns:
    if start_responsible in group and (bit & 1) != 0:
        dp[0][bit] = 1

for day in range(1, N):
    resp = S[day]
    for bit2, group2 in patterns:
        if resp not in group2:
            continue
        # 前日
        for bit1, group1 in patterns:
            if dp[day-1][bit1] == 0:
                continue
            # 活動参加者に鍵持ちがいること
            # 鍵は前日と今日の参加者に両方参加する人が必要
            if (bit1 & bit2) == 0: 
                continue
            dp[day][bit2] = (dp[day][bit2] + dp[day-1][bit1]) % MOD

ans = 0
for bit, group in patterns:
    ans = (ans + dp[N-1][bit]) % MOD

print(ans)