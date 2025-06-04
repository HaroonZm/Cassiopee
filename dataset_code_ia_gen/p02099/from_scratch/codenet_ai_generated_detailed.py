# 解説
# GPAじゃんけんは、参加者全員がそれぞれ一回ずつ対戦する総当たり戦を行う。
# GPAが高い方が勝ち、同じなら引き分け。
# 各対戦結果ごとに勝者に3点、引き分けの場合は両者に1点ずつ、敗者は0点を付与。
# これを全てのペアで実施し、各参加者の勝ち点を合計して出力する。

N = int(input())  # 参加者数
gpas = [float(input()) for _ in range(N)]  # 各参加者のGPA

# 勝ち点を格納するリストを0で初期化
points = [0] * N

# i < j のすべての組み合わせで対戦
for i in range(N):
    for j in range(i+1, N):
        if gpas[i] > gpas[j]:
            # iが勝ち、jが負け
            points[i] += 3
        elif gpas[i] < gpas[j]:
            # jが勝ち、iが負け
            points[j] += 3
        else:
            # 引き分け（同点）
            points[i] += 1
            points[j] += 1

# 各参加者の勝ち点を一行ずつ出力
for p in points:
    print(p)