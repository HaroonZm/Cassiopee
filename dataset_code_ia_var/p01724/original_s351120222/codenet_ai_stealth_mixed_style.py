def prog():
 N=20
 M=15
 grid=[[-1 for _ in range(M)] for _ in range(N)]
 count=0
 for idx in range(N-1):
    val=input()
    it=0
    while it<M:
        sym=val[it]
        if sym=='O':
            posx=it
            posy=idx
        if sym=='X':
            grid[idx][it]=count
            count+=1
        it+=1
 dirs=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
 Max=30
 memo=dict()
 def Search(bitmask,i,j):
    tup=(bitmask,i,j)
    if tup in memo: return memo[tup]
    if j>=N-2: return 0
    best=Max
    for pair in dirs:
        xi,yj=pair
        p=i+xi
        q=j+yj
        if not (0<=p<M and 0<=q<N): continue
        m=grid[q][p]
        if m==-1 or not (bitmask&(1<<m)): continue
        newState=bitmask^(1<<m)
        p+=xi
        q+=yj
        while 0<=p<M and 0<=q<N:
            m2=grid[q][p]
            if m2==-1 or not (bitmask&(1<<m2)):break
            newState^=(1<<m2)
            p+=xi
            q+=yj
        else:
            if (p==-1 or p==M) and q==N-1: return 1
            continue
        out=Search(newState,p,q)+1
        if out<best: best=out
    memo[tup]=best
    return best
 result=Search((1<<count)-1,posx,posy)
 thing=result if result<Max else -1
 print(thing)
prog()