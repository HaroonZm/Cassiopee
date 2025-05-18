N,C = map(int,input().split())
xv = [list(map(int,input().split())) for _ in range(N)]
x = [xv[i][0] for i in range(N)]
v = [xv[i][1] for i in range(N)]

C1 = [0]*N
C2 = [0]*N
for i in range(N):
    C1[i] = C1[i-1]+v[i]
    C2[i] = C2[i-1]+v[i]
for i in range(N):
    C1[i] -= x[i]
    C2[i] -= 2*x[i]
for i in range(1,N):
    C1[i] = max(C1[i],C1[i-1])
    C2[i] = max(C2[i],C2[i-1])

D1 = [0]*N
D2 = [0]*N
for i in range(N):
    D1[i] = D1[i-1]+v[N-1-i]
    D2[i] = D2[i-1]+v[N-1-i]
for i in range(N):
    D1[i] -= C-x[N-1-i]
    D2[i] -= 2*(C-x[N-1-i])
for i in range(1,N):
    D1[i] = max(D1[i],D1[i-1])
    D2[i] = max(D2[i],D2[i-1])

ans = 0
for i in range(N):
    ans = max(ans,C1[i],D1[i])

for i in range(N-1):
    ans = max(ans,C2[i]+D1[N-i-2],D2[i]+C1[N-i-2])

print(ans)