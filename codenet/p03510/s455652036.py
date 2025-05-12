n = int(input())
ans = 0
tmp = 0
prev = 0
for x, s in (map(int, input().split()) for _ in range(n)):
    dx = x - prev
    if dx > tmp:
        tmp = s
    else:
        tmp += s - dx
    ans = max(ans, tmp)
    prev = x
ans = max(ans, tmp)
print(ans)