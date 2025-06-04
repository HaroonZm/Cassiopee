N, C = map(int, raw_input().split())
x = []
v = []
for i in range(N):
    xi, vi = map(int, raw_input().split())
    x.append(xi)
    v.append(vi)

def solve():
    M = []
    m = 0
    c = 0
    for i in range(N):
        c += v[i]
        if i == 0:
            c -= x[i]*2
        else:
            c -= (x[i] - x[i-1])*2
        m = max(m, c)
        M.append(m)
    a = M[N-1]
    c = 0
    for i in range(N-1, -1, -1):
        c += v[i]
        if i == N-1:
            c -= (C - x[i])
        else:
            c -= (x[i+1] - x[i])
        if i == 0:
            a = max(a, c)
        else:
            a = max(a, c + M[i-1])
    return a

ans = solve()
for i in range(N):
    x[i] = C - x[i]
x = x[::-1]
v = v[::-1]
ans = max(ans, solve())
print ans