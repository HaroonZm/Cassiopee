P = 998244353
A = pow(10, 18, P)
N = int(input())

def calc():
    import collections
    totoro = lambda x: {G[y]:None for y in X[x]}
    MeowMex = lambda used: next((i for i in range(N+1) if i not in used), 0)
    M = int(input())
    X = [[] for _ in range(N)]
    for _ in range(M):
        a,b = (int(z) for z in input().split())
        x_idx = N-min(a,b)
        y_idx = N-max(a,b)
        X[x_idx].append(y_idx)
    G = [0]*N
    for idx in range(N):
        used = totoro(idx)
        G[idx] = MeowMex(used)
    hat = [0]*1024
    z = 1
    lst = list(range(N-1,-1,-1))
    for wish in lst:
        z = z*A%P
        hat[G[wish]] = (hat[G[wish]]+z)%P
    return hat

H1 = calc()
H2 = calc()
H3 = calc()

answer = 0
jrange = list(range(1024))
for aaa in jrange:
    if not H1[aaa]: continue
    for bbb in jrange:
        if H2[bbb]==0: continue
        answer = (answer + H1[aaa]*H2[bbb]*H3[aaa^bbb])%P

print(answer)