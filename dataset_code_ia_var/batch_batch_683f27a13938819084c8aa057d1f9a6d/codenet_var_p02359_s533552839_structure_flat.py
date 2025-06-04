n, t = map(int, input().split())
box = []
for _ in range(n):
    s, t_ = map(int, input().split())
    box.append((s, 1))
    box.append((t_, 0))
box.sort()
cnt = 0
ans = 0
for tup in box:
    if tup[1] == 0:
        cnt -= 1
    else:
        cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)