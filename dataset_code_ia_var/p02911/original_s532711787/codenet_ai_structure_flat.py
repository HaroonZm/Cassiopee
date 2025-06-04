N, K, Q = map(int, input().split())
A = []
for _ in range(Q):
    A.append(int(input()))
P = []
for _ in range(N):
    P.append(K)
for i in range(Q):
    P[A[i] - 1] += 1
for i in range(N):
    if P[i] - Q > 0:
        print("Yes")
    else:
        print("No")