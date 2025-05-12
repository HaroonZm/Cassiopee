N = int(input())

E = [[] for i in range(N + 1)]
ans = {}
First = 0
edges = 0
q = []
visited = [False] * (N + 1)

for i in range(N - 1):
    A, B = map(int, input().split())
    E[A].append(B)
    E[B].append(A)
    if len(E[A]) > edges:
        First = A
        edges = len(E[A])

    if len(E[B]) > edges:
        First = B
        edges = len(E[B])

C = list(map(int, input().split()))
C.sort()
max = sum(C) - C[-1]
q.append(First)

for i in range(1, N + 1):
    x = q.pop(0)
    visited[x] = True
    ans[x] = C[-i]
    for xx in E[x]:
        if not visited[xx]:
            q.append(xx)

print(max)

s = ""
for i in range(1, N + 1):
    s += str(ans[i])
    if i != N:
        s += " "

print(s)