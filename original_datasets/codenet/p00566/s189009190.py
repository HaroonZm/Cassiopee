h,w = map(int, input().split())
a = [list(map(int,input().split())) for i in range(h)]

ans = 1e9
for i in range(h):
    for j in range(w):
        cnt = 0
        for m,row in enumerate(a):
            for n,x in enumerate(row):
                cnt += min(abs(i-m),abs(j-n))*x
        ans = min(ans, cnt)
print(ans)