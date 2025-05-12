while 1:
    n=int(input())
    if n==0:break
    a=[list(input())for _ in [0]*n]
    for i in range(n):
        for j in range(len(a[i])):
            if a[i][j]=='.':a[i][j]=' '
            else:
                if j>0:
                    a[i][j-1]='+'
                    x=i-1
                    while a[x][j-1]==' ':
                        a[x][j-1]='|'
                        x-=1
                break
    [print(*b,sep='')for b in a]