N = int(input())

A = [[None]*N for _ in [0]*N]

def f(B,level):
    if len(B)==1 : return
    B0 = B[::2]
    B1 = B[1::2]
    for b0 in B0:
        for b1 in B1:
            A[b0][b1] = level
            A[b1][b0] = level
    f(B0,level+1)
    f(B1,level+1)

f(list(range(N)),1)

for i,a in enumerate(A[:-1]):
    print(*a[i+1:])