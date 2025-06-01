n=int(input())
c=[list(map(int,input().split())) for _ in range(10)]
patterns=[(3,[(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]),(2,[(-1,0),(0,-1),(0,0),(0,1),(1,0)]),(1,[(0,0)])]
res=[]
def can_place(x,y,s):
    for dx,dy in dict(patterns)[s]:
        nx,ny=x+dx,y+dy
        if nx<0 or nx>=10 or ny<0 or ny>=10 or c[ny][nx]==0:
            return False
    return True
def place(x,y,s):
    for dx,dy in dict(patterns)[s]:
        c[y+dy][x+dx]-=1
for _ in range(n):
    for y in range(10):
        for x in range(10):
            for s,p in patterns:
                if can_place(x,y,s):
                    place(x,y,s)
                    res.append((x,y,s))
                    break
            else:
                continue
            break
        else:
            continue
        break
for x,y,s in res:
    print(x,y,s)