N = int(input())
src = list(map(int, input().split()))
ans = -1
for i in range(N - 1):
    for j in range(i + 1, N):
        prod = src[i] * src[j]
        s = str(prod)
        increasing = True
        for k in range(len(s) - 1):
            if int(s[k]) + 1 != int(s[k + 1]):
                increasing = False
                break
        if increasing:
            if prod > ans:
                ans = prod
print(ans)