from collections import deque

n, q = list(map(int, input().split()))
L = [deque() for _ in range(n)]

for i in range(q):
    query = input()

    # insert
    if query[0] == "0":
        _, t, x = list(map(int, query.split()))
        L[t].append(x)

    # dump
    elif query[0] == "1":
        _, t = list(map(int, query.split()))
        print(*L[t])
    
    # splice
    else:
        _, s, t = list(map(int, query.split()))
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

        L[s] = deque()