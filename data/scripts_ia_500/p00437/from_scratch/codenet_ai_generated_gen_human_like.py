def main():
    while True:
        a,b,c = map(int,input().split())
        if a==0 and b==0 and c==0:
            break
        n = int(input())
        total = a+b+c
        # parts_status[i] = 0 if faulty, 1 if normal, 2 if unknown
        status = [2]*(total+1)
        tests = []
        for _ in range(n):
            i,j,k,r = map(int,input().split())
            tests.append((i,j,k,r))
        changed = True
        while changed:
            changed = False
            for i,j,k,r in tests:
                # r=1 means all 3 normal
                if r==1:
                    for x in (i,j,k):
                        if status[x]==0:
                            # conflict, but problem doesn't say contradictory input,
                            # so just continue
                            pass
                        elif status[x]==2:
                            status[x]=1
                            changed = True
                else:
                    # r=0 means at least one faulty
                    # if two are normal definitely the third is faulty
                    count_normal = 0
                    unknowns = []
                    for x in (i,j,k):
                        if status[x]==1:
                            count_normal += 1
                        elif status[x]==2:
                            unknowns.append(x)
                    if count_normal==2 and len(unknowns)==1:
                        # that unknown part must be faulty
                        x=unknowns[0]
                        if status[x]!=0:
                            status[x]=0
                            changed = True
                    # if two parts are faulty, the third normal?
                    # It can't be concluded in current logic, skip.
                    # But if one known faulty and one known normal, can we conclude?
                    # No direct info from problem statement.
                    # Just continue

        for i in range(1,total+1):
            print(status[i])

if __name__=="__main__":
    main()