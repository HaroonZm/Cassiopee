while True:
    M,T,P,R=map(int,raw_input().split())
    if M==T==P==R==0:break
    PB=[[False]*P for i in range(T+1)]
    PN=[[0]*P for i in range(T+1)]
    TM=[M]*(T+1)
    for i in range(R):
        m,t,p,r=map(int,raw_input().split())
        if r==0:
            PB[t][p-1]=True
            TM[t]+=m
        else:
            PN[t][p-1]+=1
    for i in range(1,T+1):
        for j in range(P):
            if PB[i][j]:
                TM[i]+=PN[i][j]*20
    solved=[sum(i) for i in PB]
    ans=[]
    for i in range(1,T+1):
        ans.append((-solved[i],TM[i],i))
    import operator
    ans=ans[::-1]
    ans.sort(key=operator.itemgetter(1))
    ans.sort(key=operator.itemgetter(0))
    s=str(ans[0][2])
    for i in range(1,T):
        if (ans[i][0]!=ans[i-1][0]) or (ans[i][1]!=ans[i-1][1]):
            s+=","+str(ans[i][2])
            continue
        s+="="+str(ans[i][2])
    print s