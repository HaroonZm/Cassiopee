import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.readline
readlines = sys.stdin.readlines

N = int(readline())
lines = readlines()
PQ = []
for line in lines:
    a, b = line.split()
    a = int(a) - 1
    b = int(b) - 1
    PQ.append((a, b))

graph = []
for _ in range(N):
    graph.append([])
for p, q in PQ:
    graph[p].append(q)
    graph[q].append(p)

deg = []
for x in graph:
    deg.append(len(x))

cnt_deg1 = 0
for x in deg:
    if x == 1:
        cnt_deg1 += 1

deg2_path = 0
stack = [(0, -1, 0)]
ret = [None] * N
order = []
while stack:
    x, parent, mode = stack.pop()
    if mode == 0:
        stack.append((x, parent, 1))
        for y in graph[x]:
            if y != parent:
                stack.append((y, x, 0))
    else:
        arr = []
        for y in graph[x]:
            if y != parent:
                arr.append(ret[y])
        if len(arr) == 0:
            ret[x] = 0
        elif len(arr) == 1:
            ret[x] = arr[0] + (deg[x] == 2)
        else:
            arr.sort()
            tmp = arr[-1] + arr[-2] + (deg[x] == 2)
            if tmp > deg2_path:
                deg2_path = tmp
            ret[x] = arr[-1] + (deg[x] == 2)

answer = cnt_deg1 + deg2_path
print(answer)