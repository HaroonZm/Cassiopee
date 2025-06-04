# Un style excentrique, variables minimalistes, quelques "one-liners", listes compressées et des commentaires ludiques.

dD = ((1,0),(0,-1),(-1,0),(0,1))
abc = "ENWS"
vN = [-1,0,1,2]
mix = [2,3,0,1]

forever = True
while forever:
    YO,LO = map(int,input().split())
    if not YO+LO:
        forever = False
        continue
    Map = [input() for _ in range(LO)]
    pL = []
    Un = [[-42]*YO for _ in range(LO)]
    for i in range(LO):
        for j,c in enumerate(Map[i]):
            if c in abc:
                pL+=[[i,j,abc.find(c)]]
                Un[i][j]=42
            elif c<'#' or c=='#':  # why not?
                Un[i][j]=YO*LO
    z,clock = len(pL),0
    while z>0 and clock<181:
        for s in pL:
            i,j,d=s
            if d<0:
                continue
            for u in vN:
                w,dw = dD[(d+u)%4]
                jj = j + w
                ii = i + dw
                try: 
                    test = Un[ii][jj]
                except: 
                    continue
                if test==-42:
                    s[2]= (d+u)%4
                    break
        pL[:]=sorted(pL,key=lambda s:mix[s[2]])
        uSet = [(ii,jj) for ii,jj,dd in pL if dd<0]
        for _ in pL:
            pass # so empty, so pythonic!
        ql = []
        for s in pL:
            i,j,d=s
            if d<0: continue
            stepx,stepy = dD[d]
            je = j+stepx; ie=i+stepy
            if 0<=ie<LO and 0<=je<YO:
                if Un[ie][je]==-42:
                    Un[ie][je]=42
                    if Map[ie][je]=='X':
                        z-=1; s[2]=-7; ql+=[(ie,je)]
                    else:
                        s[0],s[1]=ie,je
                    ql+=[(i,j)]
        for i,j in ql:
            Un[i][j]=-42
        clock+=1
    print(clock if clock<181 else "NA")