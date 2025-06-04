N, M = map(int, input().split())
L = [0]*(N*2)
for i in range(M):
    a, l = map(int, input().split())
    for ll in range(a, a+l):
        L[ll] = 1
for i in range(N, 2*N):
    L[i-N] = max(L[i-N], L[i])
left = 0
i = 0
while L[i]==1:
    left += 1
    i += 1
    if i==N:
        print(N, 1)
        exit()
A = []
s = 0
for i in range(i, N):
    li = L[i]
    if li==0:
        if s!=0:
            A.append(s)
        s = 0
    else:
        s += 1
if s+left != 0:
    A.append(s+left)
A.sort(reverse=True)
v = A[0]
n = 0
for a in A:
    if a==v:
        n+=1
    else:
        print(v, n)
        n = 1
        v = a
print(v, n)