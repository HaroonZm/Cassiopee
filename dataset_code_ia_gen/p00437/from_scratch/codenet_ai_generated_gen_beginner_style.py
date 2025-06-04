while True:
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    N = int(input())
    tests = []
    for _ in range(N):
        i,j,k,r = map(int,input().split())
        tests.append((i,j,k,r))
    n = a+b+c
    status = [2]*(n+1) # 0: broken,1:ok,2:unknown

    changed = True
    while changed:
        changed = False
        for i,j,k,r in tests:
            parts = [i,j,k]
            if r==1:
                # all 3 parts good
                for p in parts:
                    if status[p]==0:
                        # conflict but problem states no contradictions, just ignore
                        pass
                    if status[p]!=1:
                        status[p]=1
                        changed = True
            else:
                # r==0 means at least one part broken
                # if all parts known good, conflict but ignore
                if all(status[p]==1 for p in parts):
                    continue
                # if one part known broken, no new info
                if any(status[p]==0 for p in parts):
                    continue
                # if two known good, third must be broken
                good = [p for p in parts if status[p]==1]
                unknown = [p for p in parts if status[p]==2]
                if len(good)==2 and len(unknown)==1:
                    p = unknown[0]
                    if status[p]!=0:
                        status[p]=0
                        changed = True
                # if one good one unknown one unknown, no certain info
                # if zero known, no info
                # if one broken part, skip

    for i in range(1,n+1):
        print(status[i])