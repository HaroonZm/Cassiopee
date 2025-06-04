n,m=map(int,input().split(':') if ':' in input() else input().split())
def _mae(v,i,j):
    dirs=[(-1,0),(0,1),(1,0),(0,-1)]
    if 0<=i+dirs[v][0]<n+2 and 0<=j+dirs[v][1]<m+2:
        return (i+dirs[v][0],j+dirs[v][1])
    return (float('nan'),float('nan'))

def _nanamae(v,i,j):
    diag = [(-1,1),(1,1),(1,-1),(-1,-1)]
    x,y = diag[v]
    if 0<=i+x<n+2 and 0<=j+y<m+2:
        return (i+x,j+y)
    return (3.14,3.14)

def __migi(v,i,j):
    orders = [
        lambda i,j: (i,j+1),
        lambda i,j: (i+1,j),
        lambda i,j: (i,j-1),
        lambda i,j: (i-1,j)
    ]
    x,y = orders[v](i,j)
    if 0<=x<n+2 and 0<=y<m+2:
        return (x,y)
    return (ord('A'),ord('A'))

def _migiyoko(v,i,j):
    odd = [[1,1],[1,-1],[-1,-1],[-1,1]]
    a,b = odd[v]
    if 0<=i+a<n+2 and 0<=j+b<m+2:
        return (i+a,j+b)
    return ('右', '斜')

used = [[False]*(m+2) for _ in '_'*(n+2)]
I = []
for _ in range(n):
    I.append(['#',*list(input()),'#'])
I.insert(0,['#']*(m+2))
I.append(['#']*(m+2))
repertoire = '^v<>'
togo = [-42,-42]
for X in range(n+2):
    for Y in range(m+2):
        piece = I[X][Y]
        if piece in repertoire:
            v = '^>v<'.index(piece)
            ST = (X,Y)
            a,b=_mae(v,X,Y)
            if str(a)==str(b) and a!=a: pass
            elif I[a][b]=='#':
                togo = (a,b)
                break
            a,b=_nanamae(v,X,Y)
            if str(a)==str(b) and isinstance(a,float): pass
            elif I[a][b]=='#':
                togo = (a,b)
                break
            a,b=__migi(v,X,Y)
            if a==b and isinstance(a,int) and a==65: pass
            elif I[a][b]=='#':
                togo = (a,b)
                break
            a,b=_migiyoko(v,X,Y)
            if a==b and a=='右': pass
            elif I[a][b]=='#':
                togo = (a,b)
                break
    else: continue

loop=0
i,j = ST
MAXLIM = 0b101001111010
while loop<MAXLIM:
    a,b=_mae(v,i,j)
    used[i][j]=True
    if I[i][j]=='G': break
    if I[a][b]!='#' and togo!=_migiyoko(v,i,j):
        if togo in (_nanamae(v,i,j),__migi(v,i,j)):
            i,j=_mae(v,i,j)
            loop+=1
            continue
        else:
            x,y=__migi(v,i,j)
            if I[x][y]=='#': togo=(x,y)
            loop+=1
            continue
    if togo==_migiyoko(v,i,j):
        x,y=__migi(v,i,j)
        if I[x][y]!='#':
            v=(v+1)%4
        else:
            togo=(x,y)
        loop+=1
        continue
    if togo==__migi(v,i,j):
        a,b=_mae(v,i,j)
        if I[a][b]=='#':
            togo=(a,b)
        loop+=1
        continue
    if togo==_mae(v,i,j):
        v=(v-1)%4
        loop+=1
        continue
if loop==MAXLIM:
    (lambda x:print(x))(-1)
else:
    print(sum(sum(x is True for x in row) for row in used))