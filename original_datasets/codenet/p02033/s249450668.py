import itertools as ite
import math

INF = 10 ** 18
N, M = map(int, raw_input().split())
m = map(int, raw_input().split()) + [N + 1]
Q = input()
l = map(int, raw_input().split())
cost = [0] * (N + 1)
for i in range(M):
    cost[m[i + 1] - m[i] - 1] += 1
cost[N] += m[0] - 1
grad = 0
for i in range(N)[::-1]:
    grad += cost[i]
    cost[i] = cost[i + 1] + grad
dic = {}
S = 10 ** 5 + 1
for i in range(1, N + 1):
    if S != cost[i]:
        for j in range(cost[i], S):
            dic[j] = i
        S = cost[i]
for num in l:
    if not num in dic:
        print -1
    else:
        print dic[num]