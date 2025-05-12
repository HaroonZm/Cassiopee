import sys
input = sys.stdin.readline

M, W = map(int, input().split())                                # M: 品物の種類 W: 重量制限
single = True                                                   # True = 重複なし

price_list = [0]
weight_list = [0]
for _ in range(M):
    price, weight = map(int, input().split())
    price_list.append(price)
    weight_list.append(weight)

################################################################################################################################################

V = sum(price_list)
dp_max = W + 1                                                  # 総和重量の最大値

dp = [[dp_max] * (V + 1) for _ in range(M + 1)]                 # 左端と上端の境界条件で W, M を一個ずつ多めに取る
""" dp[item <= M ][weight <= V] = 価値を固定した時の"最小"重量 """

for item in range(M+1):                                         # 左端の境界条件
    dp[item][0] = 0                                             # 価値 0 を実現するのに必要な品物の個数は 0 個

# for weight in range(W+1):                                     # 上端の境界条件
#     dp[0][weight] = dp_min                                    # 0 種類の品物で実現できる価値総額は存在しない　（dpの初期化で自動的に課せる場合が多い）

for item in range(1,M+1):                                       # 境界条件を除いた M 回のループ（※ f[item] = g.f[item-i] の漸化式なので、list index out of range となる）
    for price in range(1, V+1):
        if price < price_list[item]:                            # price (総価値) < price_list[item] (品物の価値) の時は無視してよい
            dp[item][price] = dp[item - 1][price]
        else:
            temp = dp[item - single][price - price_list[item]] + weight_list[item]  # single = True: 重複なし
            if temp < dp[item-1][price]:                        # min(dp[item-1][price], temp)
                dp[item][price] = temp
            else:
                dp[item][price] = dp[item-1][price]

print(max(price for price in range(V+1) if dp[M][price] <= W))