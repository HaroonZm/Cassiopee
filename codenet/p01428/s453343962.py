def search(c,a,b):
    r={'o':'x','x':'o'}
    ans=0
    direct=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    for d in range(8):
        y,x=a,b
        i,j=direct[d]
        while s[y+i][x+j]==r[c]:
            y+=i
            x+=j
        if s[y+i][x+j]==c:
            ans+=max(abs(y-a),abs(x-b))

    return ans

def mami():
    m=0
    a=b=-1
    for i in range(1,9):
        for j in range(1,9):
            if s[i][j]=='.':
                t=search('o',i,j)
                if t>m:
                    m=t
                    a,b=i,j
    return(a,b)

def char():
    m=1
    a=b=-1
    for i in range(1,9):
        for j in range(1,9):
            if s[i][j]=='.':
                t=search('x',i,j)
                if t>=m:
                    m=t
                    a,b=i,j
    return(a,b)

def rev(c,a,b):
    #s[a][b]=c
    r={'o':'x','x':'o'}
    direct=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    for d in range(8):
        y,x=a,b
        i,j=direct[d]
        while s[y+i][x+j]==r[c]:
            y+=i
            x+=j
        if s[y+i][x+j]==c:
            #i,j=direct[d]
            y,x=a+i,b+j
            while s[y][x]==r[c]:
                s[y][x]=c
                y+=i
                x+=j
    s[a][b]=c

s=[['.']*10]
for _ in range(8):
    s.append(['.']+list(input())+['.'])
s=tuple(s+[['.']*10])

while 1:
    a,b=mami()
    if a>0:
        rev('o',a,b)
    c,d=char()
    if c>0:
        rev('x',c,d)
    if all(i==-1for i in(a,b,c,d)):
        break
for t in s[1:-1]:
    print(*t[1:9],sep='')