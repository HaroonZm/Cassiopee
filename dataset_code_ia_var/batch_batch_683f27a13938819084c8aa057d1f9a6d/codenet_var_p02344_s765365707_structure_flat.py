from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

sys.setrecursionlimit(1000000)
mod = 1000000007

# 1_B 重み付きunionfind, version plate

n_Q_input = sys.stdin.readline()
while n_Q_input.strip() == "":
    n_Q_input = sys.stdin.readline()
n, Q = map(int, n_Q_input.split())

par = [i for i in range(n)]
rank = [0 for i in range(n)]
w = [0 for i in range(n)]
for _ in range(Q):
    # Lire la requête par ligne
    q_line = sys.stdin.readline()
    while q_line.strip() == "":
        q_line = sys.stdin.readline()
    q = list(map(int, q_line.split()))
    if q[0]:
        x, y = q[1], q[2]
        # Calcul du root(x)
        stackx = []
        curr = x
        while par[curr] != curr:
            stackx.append(curr)
            curr = par[curr]
        r_x = curr
        while stackx:
            cx = stackx.pop()
            w[cx] += w[par[cx]]
            par[cx] = r_x

        # Calcul du root(y)
        stacky = []
        curr = y
        while par[curr] != curr:
            stacky.append(curr)
            curr = par[curr]
        r_y = curr
        while stacky:
            cy = stacky.pop()
            w[cy] += w[par[cy]]
            par[cy] = r_y

        if r_x == r_y:
            print(w[y]-w[x])
        else:
            print("?")
    else:
        x, y, z = q[1], q[2], q[3]
        # root(x)
        stackx = []
        curr = x
        while par[curr] != curr:
            stackx.append(curr)
            curr = par[curr]
        r_x = curr
        while stackx:
            cx = stackx.pop()
            w[cx] += w[par[cx]]
            par[cx] = r_x

        # root(y)
        stacky = []
        curr = y
        while par[curr] != curr:
            stacky.append(curr)
            curr = par[curr]
        r_y = curr
        while stacky:
            cy = stacky.pop()
            w[cy] += w[par[cy]]
            par[cy] = r_y

        if r_x != r_y:
            z_use = z + w[x] - w[y]
            if rank[r_x] < rank[r_y]:
                par[r_x] = r_y
                w[r_x] = -z_use
            else:
                par[r_y] = r_x
                w[r_y] = z_use
                if rank[r_x] == rank[r_y]:
                    rank[r_x] += 1