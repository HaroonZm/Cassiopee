def main():
    p=input()
    q=input()
    lp=len(p)
    lq=len(q)
    memop=[[0,0] for _ in [0]*(lp+2)]
    memoq=[[0,0] for _ in [0]*(lq+2)]
    memop[lp+1]=[lp+1,lp+1]
    memoq[lq+1]=[lq+1,lq+1]
    memop[lp]=[lp+1,lp+1]
    memoq[lq]=[lq+1,lq+1]
    
    for i in range(lp-1,-1,-1):
        if p[i]=="0":
            memop[i][0]=i+1
            memop[i][1]=memop[i+1][1]
        else:
            memop[i][0]=memop[i+1][0]
            memop[i][1]=i+1
    for i in range(lq-1,-1,-1):
        if q[i]=="0":
            memoq[i][0]=i+1
            memoq[i][1]=memoq[i+1][1]
        else:
            memoq[i][0]=memoq[i+1][0]
            memoq[i][1]=i+1
    
    dp=[dict() for _ in [0]*(lp+2)]
    dp[lp+1][lq+1]=[0,0]
    q=[[0,0]]
    while q:
        i,j=q.pop()
        if j not in dp[i].keys():
            dp[i][j]=[None,None]
            a,b=None,None
        else:
            a,b=dp[i][j]
        if a==None or b==None:
            q.append([i,j])
            if a==None:
                ap,bq=memop[i][0],memoq[j][0]
                if bq not in dp[ap].keys():
                    dp[ap][bq]=[None,None]
                    q.append([ap,bq])
                else:
                    aa,bb=dp[ap][bq]
                    if aa==None or bb==None:
                        q.append([ap,bq])
                    else:
                        dp[i][j][0]=min(aa,bb)+1
            if b==None:
                ap,bq=memop[i][1],memoq[j][1]
                if bq not in dp[ap].keys():
                    dp[ap][bq]=[None,None]
                    q.append([ap,bq])
                else:
                    aa,bb=dp[ap][bq]
                    if aa==None or bb==None:
                        q.append([ap,bq])
                    else:
                        dp[i][j][1]=min(aa,bb)+1

    q=[[0,0]]
    ans=""
    while q:
        i,j=q.pop()
        a,b=dp[i][j]
        if a==0 or b==0:
            break
        if a>b:
            q.append([memop[i][1],memoq[j][1]])
            ans+="1"
        else:
            q.append([memop[i][0],memoq[j][0]])
            ans+="0"
    print(ans)
                
if __name__=='__main__':
    main()