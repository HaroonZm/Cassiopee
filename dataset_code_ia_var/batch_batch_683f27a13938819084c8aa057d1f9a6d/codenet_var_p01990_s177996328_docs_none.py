def inpl(): return list(map(int, input().split()))
N, _ = inpl()
A = inpl()
if N == 1:
    print(*A)
    exit()
L = [0]*(N+1)
R = [0]*(N+1)
for i in range(N-1):
    R[A[i]] = A[i+1]
    L[A[i+1]] = A[i]
lm = A[0]
rm = A[-1]
for q in inpl():
    if q == rm:
        l = L[q]
        R[l] = 0
        L[q] = 0
        R[q] = lm
        L[lm] = q
        lm = q
        rm = l
    elif q == lm:
        r = R[q]
        L[r] = 0
        R[q] = 0
        L[q] = rm
        R[rm] = q
        lm = r
        rm = q
    else:
        l, r = L[q], R[q]
        L[q] = rm
        R[q] = lm
        R[l] = 0
        L[r] = 0
        L[lm] = q
        R[rm] = q
        rm = l
        lm = r
ans = []
while lm != 0:
    ans.append(lm)
    lm = R[lm]
print(*ans)