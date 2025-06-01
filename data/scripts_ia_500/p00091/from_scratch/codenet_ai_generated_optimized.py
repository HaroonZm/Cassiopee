n=int(input())
c=[list(map(int,input().split())) for _ in range(10)]

masks={1:[(0,0),(1,0),(-1,0),(0,1),(0,-1)],
       2:[(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1),(0,2),(0,-2),(2,0),(-2,0)],
       3:[(x,y) for x in range(-2,3) for y in range(-2,3) if abs(x)+abs(y)<=2]}

def valid(x,y,s):
    for dx,dy in masks[s]:
        nx,ny=x+dx,y+dy
        if nx<0 or ny<0 or nx>=10 or ny>=10:
            return False
    return True

res=[]
for _ in range(n):
    placed=False
    # Try large to small sizes for heuristics
    for size in [3,2,1]:
        for x in range(10):
            for y in range(10):
                if valid(x,y,size):
                    # Check if this placement matches the increments
                    ok=True
                    for dx,dy in masks[size]:
                        nx,ny=x+dx,y+dy
                        if c[ny][nx]==0:
                            ok=False
                            break
                    if ok:
                        # Subtract 1 to simulate removal of this drop
                        for dx,dy in masks[size]:
                            nx,ny=x+dx,y+dy
                            c[ny][nx]-=1
                        res.append((x,y,size))
                        placed=True
                        break
            if placed:
                break
        if placed:
            break
for x,y,s in res:
    print(x,y,s)