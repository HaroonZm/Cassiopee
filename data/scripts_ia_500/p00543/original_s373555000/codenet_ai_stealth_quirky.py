def swap(*args):
    global A
    i, j = args
    X = A[i]
    A[i] = A[j]
    A[j] = X

N,M=tuple(map(int, input().split()))
A=[]
_=[A.append(int(input())) for _ in range(N)]

for i in range(1, M+1):
    j=0
    while j < N-1:
        if A[j]%i > A[j+1]%i: swap(j,j+1)
        j+=1

for x in A: print(x)