import bisect

M=[]
D=[]
N=[]
count=0

def insert(M,D,N,count,key,x):
    y=bisect.bisect_left(D,key)
    if y<count and D[y]==key:
        M[y][1]=x
        N[y]=x
    else:
        M.insert(y,[key,x])
        D.insert(y,key)
        N.insert(y,x)
        count+=1
    return M,D,N,count

def get(D,N,count,key):
    y=bisect.bisect_left(D,key)
    if y<count and D[y]==key:
        print(N[y])
    else:
        print(0)

def erase(M,D,N,count,key):
    y=bisect.bisect_left(D,key)
    if y<count and D[y]==key:
        M.pop(y)
        D.pop(y)
        N.pop(y)
        count-=1
    return M,D,N,count

def dump(M,D,N,L,R):
    s=bisect.bisect_left(D,L)
    e=bisect.bisect_right(D,R)
    if e-s>0:
        for i in range(s,e):
            print(M[i][0]+" "+str(M[i][1]))

q=int(input())
for i in range(q):
    query=list(map(str,input().split()))
    query[0]=int(query[0])
    if query[0]==0:
        M,D,N,count=insert(M,D,N,count,query[1],int(query[2]))
    elif query[0]==1:
        get(D,N,count,query[1])
    elif query[0]==2:
        M,D,N,count=erase(M,D,N,count,query[1])
    else:
        dump(M,D,N,query[1],query[2])