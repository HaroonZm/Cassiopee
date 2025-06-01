W, H = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(H)]

# 領地の境界線は格子点上を北西から南東に動く
# 移動は右または下のみ
# 信夫くん（先手）が最初に動き、交互に移動する

# 盤面上の各マスについて、各プレイヤーの得点差（先手 - 後手）を計算する

# dp[i][j]はマス（i,j）からゴールまで動いた時の得点差の最大値を表す
# マスの領域はH×Wで、移動は点（0,0）から点（H,W）までの格子点上で行う
# したがって、dpテーブルはサイズ(H+1)x(W+1)とする

dp = [[0]*(W+1) for _ in range(H+1)]

# 末端から逆方向に計算する
for i in range(H, -1, -1):
    for j in range(W, -1, -1):
        if i == H and j == W:
            dp[i][j] = 0
            continue
        # 移動可能な方向を列挙
        moves = []
        if i < H:
            # 下に進む
            # 次のマスの得点は s[i][j]（現在のマスはi,jで0-index）
            # 移動によって現在プレイヤーがs[i][j]を獲得し、次の状態の得点差はdp[i+1][j]
            # 次の状態は相手のターンになるため、得点差は -dp[i+1][j] + s[i][j]
            moves.append(-dp[i+1][j] + s[i][j])
        if j < W:
            # 右に進む
            moves.append(-dp[i][j+1] + s[i][j])
        if moves:
            dp[i][j] = max(moves)

# 答えは始点での得点差dp[0][0]の絶対値
print(abs(dp[0][0]))