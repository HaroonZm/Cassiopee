defnum=999999999

def parse_input(line):
    [one, lname, eq, scale, rname] = line.split()
    exp=int( scale.split("^")[-1] )
    return lname, exp, rname

while(1):
    N=int(raw_input())
    if N==0: break
    L=[]
    names=[]
    for i in range(N):
        [lname, exp, rname]=parse_input(raw_input())
        names += [lname, rname]
        L.append([lname, rname, exp])
    names=sorted(set(names))
    m=len(names)
    A=[[defnum if i!=j else 0 for i in range(m)] for j in range(m)]
    ans="Yes"
    for l in L:
        li,ri = [names.index(name) for name in l[:2]]
        exp=l[2]
        #add
        if A[li][ri] == defnum:
            A[li][ri] = exp
            A[ri][li] = -exp
            for ab in[ [li,ri], [ri,li] ]:
                a,b=ab
                for y in range(m):
                    for x in range(m):
                        if A[y][a]!= defnum and A[b][x]!=defnum:
                            A[y][x] = A[y][a]+A[a][b]+A[b][x]
                            A[x][y] = -A[y][x]
        else:
            if A[li][ri]!=exp:
                ans="No"
                break
#    print names
#    for al in A:
#        print al
    print ans