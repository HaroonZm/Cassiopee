while(1):
    [n,m]=[int(x) for x in raw_input().split()]
    if n==0:
        break
    else:
        familymatrix=[[-100000 for x in range(n)] for y in range(n)]
        for i in range(n):
            familymatrix[i][i]=0
        namedic={}
        returned=[0 for x in range(n)]
        spacenum=0
        spacenumold=0
        for i in range(n):
            indata=raw_input()
            name=indata.strip()
            spacenum=len(indata)-len(name)
            namedic[name]=i
            for j in range(i):
                familymatrix[j][i]=familymatrix[j][i-1]+(spacenum-spacenumold)
                #if familymatrix[j][i]<0:
                #    familymatrix[j][i]=-1000000
                #if familymatrix[j][i]>0 and returned[j]:
                #    familymatrix[j][i]=-1000000
            spacenumold=spacenum
        for i in range(n):
            for j in range(i):
                if familymatrix[j][i]==0 and returned[j]==0:
                    returned[j]=1
                elif familymatrix[j][i]<0:
                    returned[j]=2
                if familymatrix[j][i]>0 and returned[j]==1:
                    familymatrix[j][i]=-1
                elif returned[j]==2:
                    familymatrix[j][i]=-1
        #for i in range(n):
        #    print familymatrix[i]
        for i in range(m):
            query=raw_input().split()
            X=namedic[query[0]]
            Y=namedic[query[-1][:-1]]
            question=' '.join(query[1:-1])
            if question == 'is a child of':
                print familymatrix[Y][X]==1
            elif question == 'is the parent of':
                print familymatrix[X][Y]==1
            elif question == 'is a sibling of':
                print (familymatrix[X][Y]==0) or (familymatrix[Y][X]==0)
            elif question == 'is a descendant of':
                print familymatrix[Y][X]>0
            elif question == 'is an ancestor of':
                print familymatrix[X][Y]>0
        print ''