n, t = map(int, input().split())
box = []
for _ in range(n):
    s, t = map(int, input().split())
    box.append((s,1))
    box.append((t,0))

box = sorted(box)
cnt = 0
ans = 0
for x in box:
    a, b = x
    if b == 0:
        cnt -= 1
    else:
        cnt += 1
    ans = max(ans,cnt)
print(ans)