N = int(input())
A = list(map(int,input().split()))
S = A[0]
for i in range(1,N):
    S = S^A[i]
B = []
for j in range(N):
    B.append(str(S^A[j]))
print(' '.join(B))