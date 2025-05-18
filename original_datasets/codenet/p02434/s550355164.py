from collections import deque
n,q = map(int,input().split())
Q = []
for i in range(n):
    Q.append(deque())
for i in range(q):
    a = input().split()
    t = int(a[1])
    if a[0] == "0":Q[t].append(a[2])
    elif a[0] == "1":print(*Q[t])
    else: Q[t].clear()