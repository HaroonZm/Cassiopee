N = int(input())
A = [int(x) for x in input().split()]

s = A[0]
ans = A[0]

for i in range(1, N):
    s += A[i]
    ans = min(ans, s // (i + 1))

print(ans)