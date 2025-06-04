N = int(input())
M = int(input())
A = list(map(int, input().split()))
sc = [0] * N

for i in range(M):
    B = list(map(int, input().split()))
    for j in range(N):
        if A[i] == B[j]:
            sc[j] = sc[j] + 1
        else:
            sc[A[i]-1] = sc[A[i]-1] + 1

for val in sc:
    print(val)