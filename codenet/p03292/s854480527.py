A = list(map(int,input().split()))

A.sort()

ans = 0
for i in range(len(A)-1):
    ans += A[i+1] - A[i]

print(ans)