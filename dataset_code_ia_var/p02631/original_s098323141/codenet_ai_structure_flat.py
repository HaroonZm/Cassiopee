N = int(input())
A = list(int(a) for a in input().split())
B = A[0]
i = 1
while i < N:
    B ^= A[i]
    i += 1
C = []
i = 0
while i < N:
    C.append(B ^ A[i])
    i += 1
i = 0
res = []
while i < N:
    res.append(str(C[i]))
    i += 1
print(' '.join(res))