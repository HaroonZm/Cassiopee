N, C = map(int, raw_input().split())
x = [0] * N
v = [0] * N
for i in range(N):
    x[i], v[i] = map(int, raw_input().split())

def solve():
    M = [0] * N
    m = 0
    c = 0
    for i in range(N):
        c += v[i]
        c -= (x[i] - (0 if i == 0 else x[i - 1])) * 2
        m = max(m, c)
        M[i] = m
    a = M[N - 1]
    c = 0
    for i in range(N - 1, -1, -1):
        c += v[i]
        c -= (C if i == N - 1 else x[i + 1]) - x[i]
        a = max(a, c + (0 if i == 0 else M[i - 1]))
    return a

ans = solve()
for i in range(N):
    x[i] = C - x[i]
x = x[::-1]
v = v[::-1]
ans = max(ans, solve())
print ans