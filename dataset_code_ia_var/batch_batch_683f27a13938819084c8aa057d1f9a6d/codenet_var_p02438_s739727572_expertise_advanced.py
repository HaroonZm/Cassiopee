from collections import deque
import sys

n, q = map(int, sys.stdin.readline().split())
L = [deque() for _ in range(n)]

for _ in range(q):
    tokens = sys.stdin.readline().split()
    cmd = tokens[0]
    if cmd == '0':
        t, x = map(int, tokens[1:])
        L[t].append(x)
    elif cmd == '1':
        t = int(tokens[1])
        print(*L[t])
    else:
        s, t = map(int, tokens[1:])
        if L[t]:
            if len(L[s]) == 1:
                L[t].append(L[s][0])
            elif len(L[t]) == 1:
                L[s].appendleft(L[t][0])
                L[t] = L[s]
            else:
                L[t].extend(L[s])
        else:
            L[t] = L[s]
        L[s].clear()