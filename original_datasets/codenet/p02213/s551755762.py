H,W=map(int,input().split())
MAP=[input() for i in range(H)]

CANGO=[[0]*W for i in range(H)]
CANGO[0][0]=1

Q=[(0,0)]

while Q:
    x,y=Q.pop()

    for tox,toy in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
        if 0<=tox<H and 0<=toy<W and CANGO[tox][toy]==0:
            if tox%4==0:
                if toy%4==0 and MAP[tox][toy]=="6":
                    CANGO[tox][toy]=1
                    Q.append((tox,toy))
                if toy%4==1 and MAP[tox][toy]=="3":
                    CANGO[tox][toy]=1
                    Q.append((tox,toy))
                if toy%4==2 and MAP[tox][toy]=="1":
                    CANGO[tox][toy]=1
                    Q.append((tox,toy))
                if toy%4==3 and MAP[tox][toy]=="4":
                    CANGO[tox][toy]=1
                    Q.append((tox,toy))
            if tox%4==2:
                if toy%4==0 and MAP[tox][toy]=="1":
                    CANGO[tox][toy]=1
                    Q.append((tox,toy))
                if toy%4==1 and MAP[tox][toy]=="3":
                    CANGO[tox][toy]=1
                    Q.append((tox,toy))
                if toy%4==2 and MAP[tox][toy]=="6":
                    CANGO[tox][toy]=1
                    Q.append((tox,toy))
                if toy%4==3 and MAP[tox][toy]=="4":
                    CANGO[tox][toy]=1
                    Q.append((tox,toy))
            if tox%4==1:
                if toy%4==0 and MAP[tox][toy]=="2":
                    CANGO[tox][toy]=1
                    Q.append((tox,toy))

                if toy%4==2 and MAP[tox][toy]=="2":
                    CANGO[tox][toy]=1
                    Q.append((tox,toy))
            if tox%4==3:
                if toy%4==0 and MAP[tox][toy]=="5":
                    CANGO[tox][toy]=1
                    Q.append((tox,toy))

                if toy%4==2 and MAP[tox][toy]=="5":
                    CANGO[tox][toy]=1
                    Q.append((tox,toy))

if CANGO[H-1][W-1]==1:
    print("YES")
else:
    print("NO")