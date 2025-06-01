n = int(input())
A = list(map(int, input().split()))

A.append(-1)
B = []
for i in range(len(A)-1):
    if A[i] != A[i+1]:
        B.append(A[i])
A = B
A.insert(0, -1)
A.append(-1)

C = []
for i in range(len(A)-2):
    if (A[i] < A[i+1]) != (A[i+1] < A[i+2]):
        C.append(A[i+1])
A = C

A.append(-1)
pairs = []
for i in range(len(A)-1):
    if A[i] < A[i+1]:
        pairs.append((A[i], 1))
    else:
        pairs.append((A[i], -1))

pairs.sort()

n = 1
n_max = 0
prev = 0
for a, s in pairs:
    if prev < a:
        if n > n_max:
            n_max = n
        prev = a
    n += s

print(n_max)