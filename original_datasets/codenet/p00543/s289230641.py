N, M = map(int, input().split())
A = [0] * N
for i in range(N):
    A[i] = int(input())

for i in range(1, M+1):
    if i == 1:
        continue
    else:
        for j in range(N-1):
            if (A[j] % i) > (A[j+1] % i):
                tmp_val = A[j]
                A[j] = A[j+1]
                A[j+1] = tmp_val

for i in range(N):
    print(A[i])