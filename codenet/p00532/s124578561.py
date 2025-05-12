N = int(input())
M = int(input())
*A, = map(int, input().split())
sc = [0]*N
for i in range(M):
    *B, = map(int, input().split())
    for j in range(N):
        if A[i] == B[j]:
            sc[j] += 1
        else:
            sc[A[i]-1] += 1
*_,=map(print, sc)