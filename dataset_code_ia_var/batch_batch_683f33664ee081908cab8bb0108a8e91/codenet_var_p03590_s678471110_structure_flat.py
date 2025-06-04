n, k = map(int, input().split())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
k_subset = [k]
i = 0
tmp = k
while tmp:
    if tmp & 1:
        x = k & ~(1 << i)
        x = x | ((1 << i) - 1)
        k_subset.append(x)
    tmp >>= 1
    i += 1
ans = 0
for x in k_subset:
    s = 0
    for a, b in ab:
        if (a | x) == x:
            s += b
    if s > ans:
        ans = s
print(ans)