while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    N=int(input())
    tests=[]
    for _ in range(N):
        i,j,k,r=map(int,input().split())
        tests.append((i,j,k,r))
    n=a+b+c
    state=[2]*(n+1)
    adj_pass=[[] for _ in range(n+1)]
    adj_fail=[[] for _ in range(n+1)]
    fail_tests=[]
    pass_tests=[]
    for i,j,k,r in tests:
        if r==1:
            pass_tests.append((i,j,k))
        else:
            fail_tests.append((i,j,k))
    # From pass tests: all three normal
    changed=True
    while changed:
        changed=False
        for i,j,k in pass_tests:
            for x in (i,j,k):
                if state[x]==0:
                    # conflict: part was known broken but pass test includes it => no solution, ignore (problem states it's consistent)
                    pass
                if state[x]!=1:
                    state[x]=1
                    changed=True
    # Now mark parts that appear in fail tests and in pass tests as normal may be contradictory
    # Use logic: from fail test, at least one is broken
    # If two of them are normal, the third must be broken
    changed=True
    while changed:
        changed=False
        for i,j,k in fail_tests:
            s=[state[i],state[j],state[k]]
            normcnt=s.count(1)
            brokcnt=s.count(0)
            unkcnt=s.count(2)
            if brokcnt>0:
                # already known broken in test, no forced change
                continue
            if normcnt==2 and unkcnt==1:
                # the unknown one must be broken
                if state[i]==2 and s.count(1)==2:
                    if state[j]==1 and state[k]==1:
                        state[i]=0
                        changed=True
                        continue
                if state[j]==2 and s.count(1)==2:
                    if state[i]==1 and state[k]==1:
                        state[j]=0
                        changed=True
                        continue
                if state[k]==2 and s.count(1)==2:
                    if state[i]==1 and state[j]==1:
                        state[k]=0
                        changed=True
                        continue
            elif normcnt==3:
                # from fail test all normal is impossible, conflict, but per problem no contradiction input
                pass
    # Output
    for i in range(1,n+1):
        print(state[i])