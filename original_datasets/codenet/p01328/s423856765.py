import bisect

def choosebait(Eloc,Clist,catinE,idinE,i):
#    dist=[abs(Clist[i][0]-x) for x in Eloc]
#    closestbaitid=dist.index(min(dist))
#    catinE[closestbaitid]+=Clist[i][2]
#    idinE[closestbaitid].append(i)

     baitid=bisect.bisect_left(Eloc,Clist[i][0])
     if baitid==0:
         leftclose=-1e10
         rightclose=Eloc[baitid]
     elif baitid==len(Eloc):
         leftclose=Eloc[baitid-1]
         rightclose=1e10
     else:
         leftclose=Eloc[baitid-1]
         rightclose=Eloc[baitid]
     if abs(Clist[i][0]-leftclose)<=abs(Clist[i][0]-rightclose):
         catinE[baitid-1]+=Clist[i][2]
         idinE[baitid-1].append(i)
     else:
         catinE[baitid]+=Clist[i][2]
         idinE[baitid].append(i)
while(1):
    [N,M]=[int(x) for x in raw_input().split()]
    if M==0:
        break
    else:
        Clist=[]
        Eloc=[]
        catinE=[0 for x in range(M)]
        idinE=[[] for x in range(M)]
        for i in range(N):
            [x,y,c]=[int(z) for z in raw_input().split()]
            Clist.append([x,y,c])
        for j in range(M):
            x=int(raw_input())
            Eloc.append(x)
        Eloc.sort()
        ans=sum([Clist[i][2] for i in range(N)])
        for i in range(N):
            choosebait(Eloc,Clist,catinE,idinE,i)
        for j in range(M-1):
            ans=min(ans,max(catinE))
            btd=catinE.index(max(catinE))
            cattomove=idinE[btd]
            Eloc=Eloc[:btd]+Eloc[btd+1:]
            catinE=catinE[:btd]+catinE[btd+1:]
            idinE=idinE[:btd]+idinE[btd+1:]
            for i in cattomove:
                choosebait(Eloc,Clist,catinE,idinE,i)
        print ans