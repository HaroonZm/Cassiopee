# E - Red Scarf

N = int(input())
A = list(int(a) for a in input().split())

B = A[0]
for i in range(1, N):
    B ^= A[i]

C = []
for i in range(N):
    C.append(B^A[i])

print(' '.join(map(str, C)))