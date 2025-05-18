flag=[0 for i in range(64)]

def Test(flag,i):
    print(flag[i])

def Set(flag,m):
    for i in m:
        flag[i]=1
    return flag

def Clear(flag,m):
    for i in m:
        flag[i]=0
    return flag

def Flip(flag,m):
    for i in m:
        if flag[i]==0:
            flag[i]=1
        else:
            flag[i]=0
    return flag

def All(flag,m):
    judge=[flag[i] for i in m]
    if all(judge)==True:
        print(1)
    else:
        print(0)

def Any(flag,m):
    judge=[flag[i] for i in m]
    if any(judge)==True:
        print(1)
    else:
        print(0)

def none(flag,m):
    judge=[flag[i] for i in m]
    if not any(judge)==True:
        print(1)
    else:
        print(0)

def Count(flag,m):
    judge=[flag[i] for i in m]
    print(judge.count(1))

def Val(flag,m):
    a=0
    for i in m:
        a+=flag[i]*2**i
    print(a)

n=int(input())
mask=[]
for i in range(n):
    m=list(map(int,input().split()))
    mask.append(m[1:])

q=int(input())
for i in range(q):
    query=list(map(int,input().split()))
    if query[0]==0:
        Test(flag,query[1])
    elif query[0]==1:
        flag=Set(flag,mask[query[1]])
    elif query[0]==2:
        flag=Clear(flag,mask[query[1]])
    elif query[0]==3:
        flag=Flip(flag,mask[query[1]])
    elif query[0]==4:
        All(flag,mask[query[1]])
    elif query[0]==5:
        Any(flag,mask[query[1]])
    elif query[0]==6:
        none(flag,mask[query[1]])
    elif query[0]==7:
        Count(flag,mask[query[1]])
    else:
        Val(flag,mask[query[1]])