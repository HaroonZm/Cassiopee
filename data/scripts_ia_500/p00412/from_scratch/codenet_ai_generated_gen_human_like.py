from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lanes = [deque() for _ in range(N)]

for _ in range(M):
    info = input().split()
    t = int(info[0])
    x = int(info[1])
    if t == 1:
        # Car x enters: find lane with fewest cars, smallest lane number if tie
        min_len = min(len(l) for l in lanes)
        for i in range(N):
            if len(lanes[i]) == min_len:
                lanes[i].append(x)
                break
    else:
        # Fueling finished in lane x: output front car and remove it
        car_num = lanes[x-1].popleft()
        print(car_num)