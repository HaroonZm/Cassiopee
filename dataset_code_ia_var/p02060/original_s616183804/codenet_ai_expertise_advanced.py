from itertools import product
from math import ceil

def inpl(): return list(map(int, input().split()))

N = int(input())
P = inpl()
T = inpl()

ceildiv = lambda x, y: (x + y - 1) // y

max_a = ceildiv(N, T[0]) + 1
cost = float('inf')

for a, b, c in product(
        range(max_a + 1),
        range(max(1, ceildiv(max(N - T[0]*a, 0), T[1]) + 1)),
        range(max(1, ceildiv(max(N - T[0]*a - T[1]*b, 0), T[2]) + 1))
    ):
    total_tea = T[0]*a + T[1]*b + T[2]*c
    if total_tea >= N:
        total_cost = P[0]*a + P[1]*b + P[2]*c
        cost = min(cost, total_cost)
        continue
    d = ceildiv(N - total_tea, T[3])
    total_cost = P[0]*a + P[1]*b + P[2]*c + P[3]*d
    cost = min(cost, total_cost)

print(cost)