S=input()
n=4
lis=[0,4,6,8]
t=1
for i in range(n**2):
    A=["A","K","I","H","A","B","A","R","A"]
    for j in range(n):
        if((i>>j)&1):
            A[lis[j]]=""
    TMP="".join(A)
    if(TMP==S):
        print("YES")
        t=0
        break
if(t==1):
    print("NO")