from collections import deque
import sys

n, q = map(int, input().split())

# Q = [[] for _ in range(n)]
Q = [deque() for _ in range(n)]
ans = []
for query in (line.split() for line in sys.stdin):
    s = int(query[1])
    if query[0] == '0':
        t = int(query[2])
        Q[s].append(t)
    elif query[0] == '1':
        # ans.append(Q[s])
        print(*Q[s])
    elif query[0] == '2':
        t = int(query[2])
        if Q[t]:
            if len(Q[s]) == 1:
                Q[t].append(Q[s][0])
            elif len(Q[t]) == 1:
                Q[s].appendleft(Q[t][0])
                Q[t] = Q[s]
            else:
                Q[t].extend(Q[s])
                
        else:
            Q[t] = Q[s]
        Q[s] = deque()

# for i in ans:
#     print(i)