n,m=map(int,input().split())
p = [list(map(int, input().split())) for _ in range(m)]
p.sort()
p.pop(0)
ans = 0
i = 0
while i < len(p):
    if p[i][0] < n:
        ans += p[i][1] - n
    else:
        break
    i += 1
print(ans)