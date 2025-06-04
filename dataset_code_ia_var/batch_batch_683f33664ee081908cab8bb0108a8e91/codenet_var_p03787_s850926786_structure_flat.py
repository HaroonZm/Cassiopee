N, M = map(int, input().split())
v = [-1 for _ in range(2 * N)]

def find(x):
    stack = []
    while v[x] >= 0:
        stack.append(x)
        x = v[x]
    for y in stack:
        v[y] = x
    return x

for _ in range(M):
    u, w = map(int, input().split())
    u -= 1
    w -= 1
    x = find(u)
    y = find(N + w)
    if x != y:
        if -v[x] < -v[y]:
            x, y = y, x
        v[x] += v[y]
        v[y] = x
    x = find(N + u)
    y = find(w)
    if x != y:
        if -v[x] < -v[y]:
            x, y = y, x
        v[x] += v[y]
        v[y] = x

alone = 0
bi = 0
unko = 0

for u in range(N):
    ru = find(u)
    rv = find(N + u)
    if v[ru] < 0 or v[rv] < 0:
        sz = -v[ru]
        if sz == 1:
            alone += 1
        elif find(u) == find(N + u):
            unko += 1
        else:
            bi += 1

ans = 0
ans += alone * N
ans += N * alone
ans -= alone * alone
ans += bi * bi * 2
ans += bi * unko
ans += unko * bi
ans += unko * unko

print(ans)