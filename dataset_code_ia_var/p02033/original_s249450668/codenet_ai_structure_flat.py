import math
INF = 10 ** 18
N, M = map(int, raw_input().split())
m = map(int, raw_input().split()) + [N + 1]
Q = input()
l = map(int, raw_input().split())
cost = [0] * (N + 1)
i = 0
while i < M:
    cost[m[i + 1] - m[i] - 1] += 1
    i += 1
cost[N] += m[0] - 1
grad = 0
i = N - 1
while i >= 0:
    grad += cost[i]
    cost[i] = cost[i + 1] + grad
    i -= 1
dic = {}
S = 10 ** 5 + 1
i = 1
while i <= N:
    if S != cost[i]:
        j = cost[i]
        while j < S:
            dic[j] = i
            j += 1
        S = cost[i]
    i += 1
idx = 0
while idx < len(l):
    num = l[idx]
    if num not in dic:
        print -1
    else:
        print dic[num]
    idx += 1