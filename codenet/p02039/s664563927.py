def inpl(): return list(map(int, input().split()))
from collections import defaultdict

G = dict()
for i in range(9):
    G[(i, 9)] = 0
    G[(9, i)] = 0
G[(9, 9)] = 0

for i in range(8)[::-1]:
    a = 8 - i
    b = -(-(8 - i)//2)
    i= i+1
    for j in range(8)[::-1]:
        if j % 2 == 1:
            j = j+1
            G[(i, j)] = G[(i, j+1)] + b
        else:
            j = j+1
            G[(i, j)] = G[(i, j+1)] + a

q = int(input())
for _ in range(q):
    a, b, c, d = inpl()
    print(G[(a, b)] - G[(c+1, b)] - G[(a, d+1)] + G[(c+1), (d+1)])