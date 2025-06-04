l, k = input().split()
l = int(l)
k = int(k)

dpW = [0] * 101
dpB = [0] * 101

dpW[0] = 1

ans = 0
for i in range(1, l + 1):
    if i >= k:
        dpB[i] = dpB[i] + dpW[i - k]
        ans = ans + dpW[i - k]
    dpB[i] = dpB[i] + dpW[i - 1]
    dpW[i] = dpW[i] + dpB[i - 1]
    ans = ans + dpW[i - 1]

print(ans)