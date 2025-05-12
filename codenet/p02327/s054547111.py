# DPL_3_B: Largest Rectangle
import sys
H, W = map(int, sys.stdin.readline().strip().split())

C = []
for h in range(H):
    c = list(map(int, sys.stdin.readline().strip().split()))
    C.append(c)

# 列方向のdp
dp = [[0] * (W + 1) for _ in range(H)]
for h in range(H):
    for w in range(W + 1):  # 長方形の面積探査時に一番右端が0だと都合がいい
        if w == W:
            dp[h][w] = 0
            continue
        if C[h][w] == 1:
           dp[h][w] = 0
        elif h == 0:  # 0行目は上の行が存在しないので別処理
           dp[0][w] = 1
        else:
           dp[h][w] = dp[h-1][w] + 1

# 長方形を求める
ans = 0
for h in range(H):
    stack = [(0, 0)]  # [(left, height)]
    for w in range(W + 1):
        if dp[h][w] >= stack[-1][1]:  # まだ長方形が決定されないとき
            stack.append((w, dp[h][w]))
        else:  # 高さが足りずに長方形が決定されるとき
            while stack[-1][1] > dp[h][w]:  # stack[0] = (0, 0) なので、 stack[0]は絶対に取り出されない
                left_pos, height = stack.pop()
                area = height * (w - left_pos)  # 長方形の面積
                ans = max(ans, area)
            stack.append((left_pos, dp[h][w]))

print(ans)