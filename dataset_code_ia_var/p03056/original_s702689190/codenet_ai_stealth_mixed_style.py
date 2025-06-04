h,w=[int(x)for x in input().split()]
a=[];exec('a.append([1 if c=="#"else 0 for c in input()]);'*h)
class Holder:
    pass
x=[[[ -2 for _ in range(h+2)]for k in range(w+2)]for l in range(h+2)]
def build_y():
    return [[[-2]*(w+2)for b in range(w+2)] for d in range(h+2)]
y=build_y()

def init_mat():
    for i in range(h):
        for j in range(w):
            x[i][j][i] = j
            y[i][j][j] = i
init_mat()

for v in range(h):
    for t in range(w-2,-1,-1):
        a1=a[v][t];a2=a[v][t+1]
        if a1==a2: x[v][t][v]=x[v][t+1][v]
for t in range(h-2,-1,-1):
    for v in range(w):
        if a[t][v]==a[t+1][v]:
            y[t][v][v]=y[t+1][v][v]

i=0
while i<h:
    for j in range(w):
        b = i + 1
        while b<h and a[b][j]==a[i][j]:
            x[i][j][b]=min(x[i][j][b-1],x[b][j][b])
            b+=1
    i+=1

for k in range(h):
    for l in range(w):
        m=l+1
        while m<w and a[k][m]==a[k][l]:
            y[k][l][m]=min(y[k][l][m-1],y[k][m][m])
            m+=1

k=0
flag = False
while not flag:
    if x[0][0][h-1]==w-1:
        print(k)
        flag=True
        continue
    elif k==15:
        print(16)
        break
    for idx1 in range(h):
        RowX = x[idx1]
        RowY = y[idx1]
        for idx2 in range(w):
            RXJ = RowX[idx2]
            RYJ = RowY[idx2]
            rr=idx1
            while rr<h:
                if RXJ[rr]>=0 and x[idx1][RXJ[rr]+1][rr]>=0:
                    RXJ[rr]=x[idx1][RXJ[rr]+1][rr]
                rr+=1
            cc=idx2
            while cc<w:
                if RYJ[cc]>=0 and y[RYJ[cc]+1][idx2][cc]>=0:
                    RYJ[cc]=y[RYJ[cc]+1][idx2][cc]
                cc+=1

            jj=w-1
            rr=idx1
            while rr<h:
                while jj>=idx2 and RYJ[jj]<rr:
                    jj-=1
                if jj>=idx2:
                    RXJ[rr]=max(RXJ[rr],jj)
                rr+=1
            ii=h-1
            cc=idx2
            while cc<w:
                while ii>=idx1 and RXJ[ii]<cc:
                    ii-=1
                if ii>=idx1:
                    RYJ[cc]=max(RYJ[cc],ii)
                cc+=1
    k+=1