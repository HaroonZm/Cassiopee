N = int(input())
A = input().split()
for i in range(N):
    A[i] = int(A[i])
result = 0
i = 1
while i < N:
    if A[i] > A[i-1]:
        result = result + 1
    i = i + 1
print(result)