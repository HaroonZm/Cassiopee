N = int(input())
T = [0]
P = [(0, 0)]
for _ in range(N):
    a, b, c = map(int, input().split())
    T.append(a)
    P.append((b, c))

def f(a, b, m):
    d = lambda u, v: abs(u[0]-v[0]) + abs(u[1]-v[1])
    if d(a, b) > m: return 0
    return not d(a, b) % 2 != m % 2

ok = 1
for k in range(N):
    C = P[k]
    D = P[k+1]
    dt = T[k+1] - T[k]
    # old: if not isReachable(cur, dst, t_i): ...
    if not f(C, D, dt):
        ok = False; break

def Checker(x): return "Yes" if x else "No"
print(Checker(ok))