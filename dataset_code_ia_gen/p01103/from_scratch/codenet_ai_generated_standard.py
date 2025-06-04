while True:
    d,w=map(int,input().split())
    if d==0 and w==0:
        break
    grid=[list(map(int,input().split())) for _ in range(d)]
    ans=0
    for y1 in range(d):
        for y2 in range(y1+2,d):
            for x1 in range(w):
                for x2 in range(x1+2,w):
                    outer=[]
                    inner=[]
                    valid=True
                    for y in range(y1,y2+1):
                        for x in range(x1,x2+1):
                            e=grid[y][x]
                            if y==y1 or y==y2 or x==x1 or x==x2:
                                outer.append(e)
                            else:
                                inner.append(e)
                    if not inner:
                        continue
                    min_outer=min(outer)
                    if any(o<=i for o in outer for i in inner if o<=i):
                        # check if outermost cells are all strictly greater than all inner cells
                        valid=False
                    if valid:
                        if min_outer>max(inner):
                            capacity=sum(min_outer - i for i in inner)
                            if capacity>ans:
                                ans=capacity
    print(ans)