N,H = map(int,input().split())
ab = [list(map(int,input().split())) for _ in [0]*N]

a = max([a for a,b in ab])
b = sorted([b for _,b in ab if b>a])[::-1]
s = sum(b)
if s >= H:
    while s>=H:
        s -= b.pop()
    ans = len(b)+1
else:
    ans = (H-s-1)//a+1+len(b)
print(ans)