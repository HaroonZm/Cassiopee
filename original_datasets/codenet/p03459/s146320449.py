# author:  Taichicchi
# created: 27.09.2020 23:57:30

import sys

N = int(input())

t1, x1, y1 = 0, 0, 0

for i in range(N):
    t, x, y = map(int, input().split())
    dx = abs(x - x1)
    dy = abs(y - y1)
    dt = t - t1
    d = dx + dy
    # print(f"{dt=}{d=}")

    if (d <= dt) & (dt % 2 == d % 2):
        pass
    else:
        print("No")
        exit()

    t1, x1, y1 = t, x, y

print("Yes")