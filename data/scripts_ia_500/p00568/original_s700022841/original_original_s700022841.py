H, W = list(map(int, input().split(' ')))
A = [list(map(int, input().split(' '))) for _ in range(H)]

# パスの長さはすべての場所を通る H*W が最大
# 北西の端からそのマスへのパスで, 長さがその自然数であるもののうちで, そのパス上の木をすべて伐採するのにかかる時間の最小値
dp = [[[float('inf') for l in range(H*W)] for w in range(W)] for h in range(H)]
dp[0][0][0] = 0

for l in range(1, H*W): # パスの長さ
    cont_flag = False
    for h in range(H):
        for w in range(W):
            if w + h > l:
                cont_flag = True
                continue
            surs = [sur for sur in [(h-1, w), (h+1, w), (h, w-1), (h, w+1)] if (0 <= sur[0] and sur[0] < H and 0 <= sur[1] and sur[1] < W)]
            min_cost = float('inf')
            for hs, ws in surs:
                min_cost = min(min_cost, A[h][w]*(l-1)*2 + A[h][w] + dp[hs][ws][l-1])

            dp[h][w][l] = min_cost
        if cont_flag: continue

print(min(dp[H-1][W-1]))