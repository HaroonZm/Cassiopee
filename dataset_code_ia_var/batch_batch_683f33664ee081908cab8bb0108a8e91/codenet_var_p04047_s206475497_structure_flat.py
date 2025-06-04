N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
i = 0
while i < 2*N:
    if i % 2 == 0:
        ans += L[i]
    i += 1
print(ans)