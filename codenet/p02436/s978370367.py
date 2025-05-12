from collections import deque
n, c = [int(x) for x in input().split()]
Q = []
for _ in range(n):
    Q.append(deque())
for _ in range(c):
    p, t, x = [int(_) for _ in (input()+" 0").split()][:3]
    if p == 0:
        Q[t].append(x)
    elif p == 1:
        try:
            print(Q[t][0])
        except IndexError:
            pass
    elif p == 2:
        try:
            Q[t].popleft()
        except IndexError:
            pass