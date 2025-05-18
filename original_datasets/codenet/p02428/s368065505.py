n=int(input())
temp0=input().split( )
k=int(temp0[0])
T=[int(s) for s in temp0[1:]]

m=2**n
for i in range(m):
    temp=[0 for i in range(n)]
    j=i
    count=0
    while j>0:
        if j%2==1:
            temp[count]=1
        j//=2
        count+=1
    flag=True
    for t in T:
        if temp[t]==0:
            flag=False
    if flag:
        temp2=[]
        for k in range(n):
            if temp[k]==1:
                temp2.append(k)
        print(i,end="")
        if i!=0:
            print(":",end=" " )
            print(*temp2)
        else:
            print(":")