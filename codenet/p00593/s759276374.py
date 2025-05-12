case=1
while True:
    n=input()
    if n==0:break
    value=1
    grid=[[0]*n for i in range(n)]
    x=y=0
    if n==1:
        grid[y][x]=1
    while value<n*n:
        grid[y][x]=value
        if x<n-1:
            x+=1
            value+=1
            grid[y][x]=value
        else:
            y+=1
            value+=1
            grid[y][x]=value
        while x>0 and y<n-1:
            y+=1
            x-=1
            value+=1
            grid[y][x]=value
        if y<n-1:
            y+=1
            value+=1
            grid[y][x]=value
        else:
            x+=1
            value+=1
            grid[y][x]=value
        while y>0 and x<n-1:
            y-=1
            x+=1
            value+=1
            grid[y][x]=value
    print "Case %d:"%case
    for i in range(n):
        print "%3d"*n%tuple(grid[i])
    case+=1