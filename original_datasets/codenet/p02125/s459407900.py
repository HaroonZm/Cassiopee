x = int(input())
ans = 0
i = 0
while (1 << i) <= x:
    if x & (1 << i):
        ans += 1
    i += 1
print(max(ans, i - 1))