for i in range(input()):
    cx=cy=0
    maxValue=mx=my=0
    while True:
        dx,dy=map(int,raw_input().split())
        if dx==dy==0:break
        cx+=dx
        cy+=dy
        d=cx*cx+cy*cy
        if d>maxValue or (d==maxValue and cx>mx):
            maxValue=d
            mx,my=cx,cy
    print mx,my