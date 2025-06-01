from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lanes = [deque() for _ in range(N)]

for _ in range(M):
    t, x = map(int, input().split())
    if t == 1:
        # 入場車両: 最も車が少ないレーンの末尾に追加
        min_len = min(len(l) for l in lanes)
        for i, lane in enumerate(lanes):
            if len(lane) == min_len:
                lane.append(x)
                break
    else:
        # 給油終了: lane xの先頭車両取り出し
        car = lanes[x-1].popleft()
        print(car)