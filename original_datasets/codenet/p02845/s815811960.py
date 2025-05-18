n = int(input())
L = [-1,-1,-1]
ans = 1
color = list(map(int,input().split()))
for i in range(n):
    k = L.count(color[i]-1)
    ans = (ans*k)%(10**9+7)
    for j in range(3):
        if L[j] == color[i]-1:
            L[j] += 1
            break
print(ans)