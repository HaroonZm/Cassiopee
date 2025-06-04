def go(human):
    if human[2]==0:
        if(human[1]*2-1>=0 and wall[human[1]*2-1][human[0]]=='1'):
            return 3
        elif (human[0]<=3 and wall[human[1]*2][human[0]]=='1'):
            return 0
        elif (human[1]*2+1<=8 and wall[human[1]*2+1][human[0]]=='1'):
            return 1
        else:
            return 2
    if human[2]==1:
        if(human[0]<=3 and wall[human[1]*2][human[0]]=='1'):
            return 3
        elif (human[1]*2+1<=8 and wall[human[1]*2+1][human[0]]=='1'):
            return 0
        elif (human[0]-1>=0 and wall[human[1]*2][human[0]-1]=='1'):
            return 1
        else:
            return 2
    if human[2]==2:
        if(human[1]*2+1<=8 and wall[human[1]*2+1][human[0]]=='1'):
            return 3
        elif (human[0]-1>=0 and wall[human[1]*2][human[0]-1]=='1'):
            return 0
        elif (human[1]*2-1>=0 and wall[human[1]*2-1][human[0]]=='1'):
            return 1
        else:
            return 2
    if human[2]==3:
        if(human[0]-1>=0 and wall[human[1]*2][human[0]-1]=='1'):
            return 3
        elif (human[1]*2-1>=0 and wall[human[1]*2-1][human[0]]=='1'):
            return 0
        elif (human[0]<=3 and wall[human[1]*2][human[0]]=='1'):
            return 1
        else:
            return 2

wall=[]
while True:
    try:
        for i in range(9):
            wall.append(raw_input())
    except:
        break

solve="R"
human=(1,0,0)
while human[0]!=0 or human[1]!=0:
    direction=(human[2]+go(human))%4
    if direction == 0:
        human=(human[0]+1,human[1],direction)
        solve+="R"
    elif direction == 1:
        human=(human[0],human[1]+1,direction)
        solve+="D"
    elif direction == 2:
        human=(human[0]-1,human[1],direction)
        solve+="L"
    else:
        human=(human[0],human[1]-1,direction)
        solve+="U"
print solve