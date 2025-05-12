n,m=map(int,input().split())
def mae(v,i,j):
    if v==0 and 0<=i-1<n+2 and 0<=j<m+2:
        return (i-1,j)
    elif v==1 and 0<=i<n+2 and 0<=j+1<m+2:
        return (i,j+1)
    elif v==2 and 0<=i+1<n+2 and 0<=j<m+2:
        return (i+1,j)
    elif v==3 and 0<=i<n+2 and 0<=j-1<m+2:
        return (i,j-1)
    else:
        return (-1,-1)

def nanamemae(v,i,j):
    if v==0 and 0<=i-1<n+2 and 0<=j+1<m+2:
        return (i-1,j+1)
    elif v==1 and 0<=i+1<n+2 and 0<=j+1<m+2:
        return (i+1,j+1)
    elif v==2 and 0<=i+1<n+2 and 0<=j-1<m+2:
        return (i+1,j-1)
    elif v==3 and 0<=i-1<n+2 and 0<=j-1<m+2:
        return (i-1,j-1)
    else:
        return (-1,-1)

def migi(v,i,j):
    if v==0 and 0<=i<n+2 and 0<=j+1<m+2:
        return (i,j+1)
    elif v==1 and 0<=i+1<n+2 and 0<=j<m+2:
        return (i+1,j)
    elif v==2 and 0<=i<n+2 and 0<=j-1<m+2:
        return (i,j-1)
    elif v==3 and 0<=i-1<n+2 and 0<=j<m+2:
        return (i-1,j)
    else:
        return (-1,-1)

def migiushiro(v,i,j):
    if v==0 and 0<=i+1<n+2 and 0<=j+1<m+2:
        return (i+1,j+1)
    elif v==1 and 0<=i+1<n+2 and 0<=j-1<m+2:
        return (i+1,j-1)
    elif v==2 and 0<=i-1<n+2 and 0<=j-1<m+2:
        return (i-1,j-1)
    elif v==3 and 0<=i-1<n+2 and 0<=j+1<m+2:
        return (i-1,j+1)
    else:
        return (-1,-1)

used=[[False for i in range(m+2)] for i in range(n+2)]
field=[['#']+list(input())+['#'] for i in range(n)]
field.insert(0,['#' for i in range(m+2)])
field.append(['#' for i in range(m+2)])
p=(-1,-1)
for i in range(n+2):
    for j in range(m+2):
        if field[i][j] in '^v<>':
            if field[i][j]=='^':
                v=0
            elif field[i][j]=='v':
                v=2
            elif field[i][j]=='>':
                v=1
            else:
                v=3
            st=(i,j)
            a,b=mae(v,i,j)
            if not a==b==-1 and field[a][b]=='#':
                p=(a,b)
                break
            a,b=nanamemae(v,i,j)
            if not a==b==-1 and field[a][b]=='#':
                p=(a,b)
                break
            a,b=migi(v,i,j)
            if not a==b==-1 and field[a][b]=='#':
                p=(a,b)
                break
            a,b=migiushiro(v,i,j)
            if not a==b==-1 and field[a][b]=='#':
                p=(a,b)
                break
    else:
        continue

count=0
i,j=st
inf=5242
while count<inf:
    a,b=mae(v,i,j)
    used[i][j]=True
    if field[i][j]=='G':
        break
    if field[a][b]!='#' and p!=migiushiro(v,i,j):
        if (p==nanamemae(v,i,j) or p==migi(v,i,j)):
            i,j=mae(v,i,j)
            count+=1
            continue
        else:
            x,y=migi(v,i,j)
            if field[x][y]=='#':
                p=(x,y)
            count+=1
            continue
    if p==migiushiro(v,i,j):
        x,y=migi(v,i,j)
        if field[x][y]!='#':
            v=(v+1)%4
        else:
            p=(x,y)
        count+=1
        continue
    if p==migi(v,i,j):
        a,b=mae(v,i,j)
        if field[a][b]=='#':
            p=(a,b)
        count+=1
        continue
    if p==mae(v,i,j):
        v=(v-1)%4
        count+=1
        continue
if count==inf:
    print(-1)
else:
    ans=0
    for f in used:
        for k in f:
            if k:
                ans+=1
    print(ans)