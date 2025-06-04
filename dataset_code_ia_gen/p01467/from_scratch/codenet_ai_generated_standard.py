A,B,K=map(int,input().split())
A_d= list(map(int,str(A)[::-1]))
B_d= list(map(int,str(B)[::-1]+ '0'*(len(A_d)-len(str(B)))))
n=len(A_d)
max_res=0
for mask in range(1<<n):
    if bin(mask).count('1')>K: continue
    borrow= [0]*(n+1)
    C=[0]*n
    valid=True
    for i in range(n):
        borrow_i1= 0
        a= A_d[i]-borrow[i]
        b= B_d[i]
        forgot= bool(mask & (1<<i))
        if not forgot:
            if a>=b:
                C[i]=a-b
                borrow[i+1]=0
            else:
                C[i]= a+10 -b
                borrow[i+1]=1
        else:
            # borrow forgotten
            if a>=b:
                C[i]=a-b
                borrow[i+1]=0
            else:
                C[i]= a+10 -b
                borrow[i+1]=0
    while len(C)>1 and C[-1]==0:
        C.pop()
    val=0
    for d in C[::-1]:
        val= val*10 + d
    if val>max_res:
        max_res=val
print(max_res)