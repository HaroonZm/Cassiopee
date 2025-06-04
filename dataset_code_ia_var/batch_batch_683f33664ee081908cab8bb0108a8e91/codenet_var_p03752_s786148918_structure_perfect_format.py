import sys

N, K = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))

ans = float('inf')
for i in range(2 ** (N - 1)):
    bit = [(i >> j) & 1 for j in range(N - 1)]
    can_see = 0
    cost = 0
    height = a[0]
    for j, b in enumerate(bit):
        if (b == 1) and (height >= a[j + 1]):
            cost += height - a[j + 1] + 1
            height += 1
            can_see += 1
        elif b == 1:
            height = a[j + 1]
            can_see += 1
        elif height < a[j + 1]:
            can_see += 1
        height = max(height, a[j + 1])
    if can_see >= K - 1:
        ans = min(ans, cost)

print(ans)