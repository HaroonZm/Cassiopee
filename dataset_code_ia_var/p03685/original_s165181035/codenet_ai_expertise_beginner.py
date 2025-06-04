import os
import sys
from collections import deque, Counter

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

R, C, N = map(int, sys.stdin.readline().split())
XY = []
for _ in range(N):
    XY.append(list(map(int, sys.stdin.readline().split())))

p1 = []
p2 = []
p3 = []
p4 = []

for i in range(N):
    x1, y1, x2, y2 = XY[i]
    for (x, y) in [(x1, y1), (x2, y2)]:
        if y == 0:
            p1.append((x, i))
        elif x == R:
            p2.append((y, i))
        elif y == C:
            p3.append((x, i))
        elif x == 0:
            p4.append((y, i))

p1.sort()
p2.sort()
p3.sort(reverse=True)
p4.sort(reverse=True)

points = p1 + p2 + p3 + p4
id_list = []
for pair in points:
    id_list.append(pair[1])
counts = Counter(id_list)

que = deque()
for pair in points:
    i = pair[1]
    if counts[i] <= 1:
        continue
    if len(que) > 0 and que[-1] == i:
        que.pop()
    else:
        que.append(i)

while len(que) >= 2 and que[0] == que[-1]:
    que.popleft()
    que.pop()

if len(que) == 0:
    print("YES")
else:
    print("NO")