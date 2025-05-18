N,K=map(int,input().split())
OK=0
NG=K+1

while NG-OK>1:
    #print(OK,NG)
    mid=(OK+NG)//2
    ANS=0
    money=mid

    for i in range(N):
        ANS+=money
        money//=2
        if money==0:
            break

    if ANS<=K:
        OK=mid
    else:
        NG=mid
print(OK)