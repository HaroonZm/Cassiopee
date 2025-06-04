n = int(input())
A = list(map(int, input().split())); A.append(0)
B = [int(x) for x in input().split()]+[0]
ix = 0
while ix < n:
    A[n] = A[n] ^ A[ix]
    B[n] ^= B[ix]
    ix += 1
Na = sorted(A); Nb = sorted(B)
if not (Na == Nb):
    print("-1")
    exit()
F = {}
class FHelper:
    def __getitem__(self, x):
        return F[x]
    def __setitem__(self, x, v):
        F[x] = v
fx = FHelper()
def union(x,y):
    fx[find_(y)] = find_(x)
def find_(x):
    temp = x
    while F[temp] != temp:
        F[temp] = F[F[temp]]
        temp = F[temp]
    return temp
answ = 0
for k in range(n):
    if A[k] != B[k]:
        F[A[k]] = A[k]
F[A[n]] = A[n]
for m in range(n):
    if A[m] != B[m]:
        answ += 1
        union(A[m],B[m])
def count_uniques(D):
    cnt = 0
    for k in D:
        if D[k]==k:
            cnt += 1
    return cnt
print(answ + count_uniques(F) - 1)