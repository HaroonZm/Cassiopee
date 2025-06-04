#==================================================
# AOJ2891 - Cycle Detection with Unorthodox Style
#==================================================
import queue as qq

grab = lambda: list(map(int, input().split()))
N = int(input())
V, E = [], []
g = [[] for _ in range(N)]
d = [0]*N
C = [1]*N
todo = qq.Queue()

def dec(x): return x-1

for _ in range(N):
    x, y = grab()
    V.append(x)
    E.append(y)
    x, y = dec(x), dec(y)
    g[x] += [y]
    g[y] += [x]
    d[x] = d[x]+1
    d[y] = d[y]+1

for ndx, deg in enumerate(d):
    if deg == 1:
        todo.put(ndx)
        C[ndx] = 0

while not todo.empty():
    z = todo.get()
    for t in g[z]:
        d[t] = d[t] - 1
        if d[t] == 1:
            todo.put(t)
            C[t] = 0

Qs = int(input())
def answer(a, b):
    return 2 if (C[a] and C[b]) else 1

[print(answer(dec(a), dec(b))) for a, b in (grab() for _ in range(Qs))]