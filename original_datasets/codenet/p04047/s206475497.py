N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(2*N):
    if i%2==0:
        ans += L[i]
print(ans)