N = int(input())
M = int(input())
A = input().split()
A = list(map(int, A))
S = []
for i in range(N):
    S.append(0)

for i in range(M):
    B = input().split()
    B = list(map(int, B))
    for j in range(N):
        if B[j] == A[i]:
            S[j] = S[j] + 1
    count = 0
    for x in B:
        if x == A[i]:
            count = count + 1
    S[A[i] - 1] = S[A[i] - 1] + (N - count)

for i in range(N):
    print(S[i])