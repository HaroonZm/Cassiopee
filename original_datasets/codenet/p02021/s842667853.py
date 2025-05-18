N = int(input())
A = [int(x) for x in input().split()]

sum = A[0]
ans = A[0]

for i in range(1, N):
    sum += A[i]
    ans = min(ans, sum // (i + 1))

print(ans)