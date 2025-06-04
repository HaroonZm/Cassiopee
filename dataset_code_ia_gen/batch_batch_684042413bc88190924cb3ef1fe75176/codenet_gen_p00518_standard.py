N=int(input())
S=input()
MOD=10007

# 部員のbit: J=1, O=2, I=4
char_to_bit={'J':1,'O':2,'I':4}

dp=[ [0]*8 for _ in range(N) ]

# 初期状態 鍵はJが持っている → 参加者にはJが含まれている必要がある
# 1日目の責任者も参加しなければならない
first_responsible_bit=char_to_bit[S[0]]
for state in range(1,8):
    if (state & 1) and (state & first_responsible_bit):
        dp[0][state]=1

for i in range(1,N):
    res_bit=char_to_bit[S[i]]
    for prev_state in range(1,8):
        if dp[i-1][prev_state]==0:
            continue
        for curr_state in range(1,8):
            # 今の日の責任者は必ず参加
            if (curr_state & res_bit)==0:
                continue
            # 参加者は空集合でない
            # 鍵は必ず前日と今日の参加者のいずれか
            # 鍵は前日の参加者の誰かから今日の参加者の誰かに渡るので
            # 前日と今日の参加者の共通メンバーが少なくとも1人必要
            if (prev_state & curr_state)==0:
                continue
            dp[i][curr_state]=(dp[i][curr_state]+dp[i-1][prev_state])%MOD

print(sum(dp[N-1])%MOD)