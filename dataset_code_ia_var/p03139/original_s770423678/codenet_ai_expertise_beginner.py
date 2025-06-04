N, A, B = input().split()
N = int(N)
A = int(A)
B = int(B)

if A >= B:
    print(B, end=' ')
else:
    print(A, end=' ')

if A + B - N >= 0:
    print(A + B - N)
else:
    print(0)