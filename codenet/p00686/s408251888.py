while True:
    w,h=map(int,raw_input().split())
    if w==h==0:break
    mv=((0,1),(1,0),(0,-1),(-1,0))
    pos=0
    nx=ny=1
    while True:
        command=raw_input()
        if command=="STOP":
            break
        if command[-1].isdigit():
            d,l=command.split()
            if d=="FORWARD":
                nx+=mv[pos][0]*int(l)
                ny+=mv[pos][1]*int(l)
            elif d=="BACKWARD":
                nx-=mv[pos][0]*int(l)
                ny-=mv[pos][1]*int(l)
            nx=min(nx,w)
            nx=max(nx,1)
            ny=min(ny,h)
            ny=max(ny,1)
        else:
            if command=="LEFT":
                pos=pos-1 if pos!=0 else 3
            elif command=="RIGHT":
                pos=(pos+1)%4
    print nx,ny