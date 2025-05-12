import sys
import math
input = sys.stdin.readline

N = int(input())
xy = []
sm = 0
for _ in range(N):
    xy.append(list(map(int, input().split())))
for i in range(N):
    now_x = xy[i][0]
    now_y = xy[i][1]
    for j in range(N):
        if j != i:
            sm += math.sqrt((now_x - xy[j][0])**2 + (now_y - xy[j][1])**2)
print(sm / N)