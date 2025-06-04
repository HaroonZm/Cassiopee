import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    S = input().strip()
    if len(S) < 4:
        print(S)
        continue
    es = set()
    cars = set()
    l = len(S)
    for i in range(l):
        if not 'a' <= S[i] <= 'z':
            continue
        s = S[i]
        if i + 3 >= l:
            break
        t = S[i + 3]
        cars.add(s)
        cars.add(t)
        if S[i + 1] == '-':
            es.add((s, t))
        else:
            es.add((t, s))
    cars = list(cars)
    V = len(cars)
    mapping = {}
    num = 0
    for c in cars:
        mapping[c] = num
        num += 1
    rev_mapping = {}
    for c in mapping:
        rev_mapping[mapping[c]] = c
    es_list = []
    for s, t in es:
        es_list.append((mapping[s], mapping[t]))
    in_degree = [0] * V
    out_edge = [[] for _ in range(V)]
    for s, t in es_list:
        out_edge[s].append(t)
        in_degree[t] += 1
    processed = [False] * V
    result = []
    q = deque()
    for i in range(V):
        if in_degree[i] == 0 and not processed[i]:
            q.append(i)
            processed[i] = True
            while q:
                u = q.popleft()
                result.append(u)
                for e in out_edge[u]:
                    in_degree[e] -= 1
                    if in_degree[e] == 0 and not processed[e]:
                        processed[e] = True
                        q.append(e)
    txt = []
    for x in result:
        txt.append(rev_mapping[x])
    print(''.join(txt))