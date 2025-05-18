N = int(input())
A = []
B = []

for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

c = 0

A = A[::-1]
B = B[::-1]

# print(A)
# print(B)

for i in range(N):
    ai = A[i] + c
    if ai % B[i] == 0:
        pass
    else:
        tmp = B[i] - (ai % B[i])
        c += tmp

print(c)