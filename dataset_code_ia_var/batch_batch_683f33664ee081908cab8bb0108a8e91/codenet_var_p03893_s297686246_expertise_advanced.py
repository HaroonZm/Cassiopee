x = int(input())
ans = 2
for _ in range(x):
    ans = (ans << 1) + 2
print(ans)