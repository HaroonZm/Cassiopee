a,b = map(int, input().split())
ans = 0
for i in range(a,b+1):
    s = str(i)
    hl = len(s)//2
    if s[:hl]== s[-1:-1-hl:-1]:
        ans+=1
print(ans)