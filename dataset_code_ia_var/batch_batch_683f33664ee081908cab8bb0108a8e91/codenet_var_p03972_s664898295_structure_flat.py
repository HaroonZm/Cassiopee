import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

W,H = map(int,input().split())
P = []
for _ in range(W):
    P.append(int(input()))
Q = []
for _ in range(H):
    Q.append(int(input()))
cost = 0
rest_P = W
rest_Q = H
P.sort()
Q.sort()
INF = 10**10
P.append(INF)
Q.append(INF)
p = 0
q = 0
i = 0
while i < W+H:
    x = P[p]
    y = Q[q]
    if x < y:
        cost += x * (rest_Q+1)
        p += 1
        rest_P -= 1
    else:
        cost += y * (rest_P+1)
        q += 1
        rest_Q -= 1
    i += 1
print(cost)