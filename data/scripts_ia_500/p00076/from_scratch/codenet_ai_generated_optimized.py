import sys
import math

def solve(n):
    angle = math.radians(90)
    # ベクトル v は井戸から東 1m の地点から真っ直ぐ井戸方向（西方向）
    v = (-1.0, 0.0)
    # 初期位置は東に1mの地点
    x, y = 1.0, 0.0
    # 向きは井戸方向(西)を向いたまま初期化
    direction = v
    for _ in range(n):
        # 1. 井戸方向を向く：vは既に向いているのでそのまま
        # 2. 右回り90度回転
        direction = (direction[1], -direction[0])
        # 3. 1m直進
        x += direction[0]
        y += direction[1]
        # 4. 井戸方向を向く（west方向(-1,0)）
        direction = v
    return x, y

for line in sys.stdin:
    n=line.strip()
    if n == '-1':
        break
    n=int(n)
    x,y=solve(n)
    print(f"{x:.2f}")
    print(f"{y:.2f}")