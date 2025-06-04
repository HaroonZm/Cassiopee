import bisect
def nCr(n, r):
    r = min(r, n-r)
    numerator = 1
    for i in range(n, n-r, -1):
        numerator *= i
    denominator = 1
    for i in range(r, 1, -1):
        denominator *= i
    return numerator // denominator

n,m,l=map(int,input().split())
data = [[0 for i in range(m+1)]for i in range(n)]
for i in range(n):
    p,t,v=map(int,input().split())
    for j in range(m+1):
        data[i][j]=((t*j+l/v)if v!=0 else 9999999999999999, (p/100.0)**(j) * nCr(m,j) * (1-p/100.0)**(m-j))

ans=[]
for i in range(n):
    win=0
    for j in range(m+1):
        wintmp=data[i][j][1]
        for x in range(n):
            if i==x:
                continue
            tmp=0
            for a,b in data[x][bisect.bisect_right(data[x],(data[i][j][0],5)):]:
                tmp+=b
            wintmp*=tmp
        win+=wintmp
    ans.append(win)

for a in ans:
    print('%.8f'%a)