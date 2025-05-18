N = int(input())
A = list(map(int,input().split()))

B = []
for i in range(N):
    B.append(A[i]-i)
B.sort()
b = B[N//2]-1

ans = 0
for i in range(N):
    ans += abs(A[i] - (b + i + 1))
print(ans)