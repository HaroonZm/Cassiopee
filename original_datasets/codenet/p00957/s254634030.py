l, k = map(int, input().split())

dpW = [0] * 101
dpB = [0] * 101

dpW[0] = 1

ans = 0
for i in range(1, l + 1):
    if i >= k:
        dpB[i] += dpW[i - k]
        ans += dpW[i - k]
        
    dpB[i] += dpW[i - 1]
    dpW[i] += dpB[i - 1]
    ans += dpW[i - 1]

print(ans)