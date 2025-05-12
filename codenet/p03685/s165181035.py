import os
import sys
from collections import deque, Counter

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

R, C, N = list(map(int, sys.stdin.buffer.readline().split()))
XY = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(N)]

# 入力と答えの制約より、もし長方形の制限がなければ任意の点まで行ける
# 長方形の辺上にある点だけ考えればいい

p1 = []
p2 = []
p3 = []
p4 = []
for i, (x1, y1, x2, y2) in enumerate(XY):
    for x, y in ((x1, y1), (x2, y2)):
        if y == 0:
            p1.append((x, i))
        elif x == R:
            p2.append((y, i))
        elif y == C:
            p3.append((x, i))
        elif x == 0:
            p4.append((y, i))
# 順番に並ぶようにする
p1.sort()
p2.sort()
p3.sort(reverse=True)
p4.sort(reverse=True)

points = p1 + p2 + p3 + p4
counts = Counter([i for _, i in points])
que = deque()
for _, i in points:
    if counts[i] <= 1:
        continue
    if que and que[-1] == i:
        que.pop()
    else:
        que.append(i)

while len(que) >= 2 and que[0] == que[-1]:
    que.popleft()
    que.pop()

ok = len(que) == 0
if ok:
    print('YES')
else:
    print('NO')