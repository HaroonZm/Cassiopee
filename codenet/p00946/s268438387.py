N,M = map(int,input().split())
used = [1] + [0] * N
src = [int(input()) for i in range(M)]
for v in reversed(src):
    if used[v]: continue
    print(v)
    used[v] = 1
for v,u in enumerate(used):
    if not u: print(v)