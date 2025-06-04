def isX(xy1,xy2):
    ax,ay,bx,by = xy1; cx,cy,dx,dy = xy2
    tc=(ax-bx)*(cy-ay)+(ay-by)*(ax-cx)
    td=(ax-bx)*(dy-ay)+(ay-by)*(ax-dx)
    return tc*td < 0

def ip(xy1,xy2):
    ax,ay,bx,by = xy1; cx,cy,dx,dy = xy2
    dn = ((by-ay)*(dx-cx)-(bx-ax)*(dy-cy))*1.0
    x = ((cy*dx-cx*dy)*(bx-ax)-(ay*bx-ax*by)*(dx-cx))/dn
    y = ((cy*dx-cx*dy)*(by-ay)-(ay*bx-ax*by)*(dy-cy))/dn
    return x,y

while 1:
    xy1 = map(int,raw_input().split())
    if xy1.count(0) == 4: break
    xy2 = map(int,raw_input().split())
    xy3 = map(int,raw_input().split())
    if isX(xy1,xy2) and isX(xy2,xy3) and isX(xy3,xy1):
        x1,y1 = ip(xy1,xy2); x2,y2 = ip(xy2,xy3); x3,y3 = ip(xy3,xy1)
        S = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2.0
        if   S >= 1900000: print "dai-kichi"
        elif S >= 1000000: print "chu-kichi"
        elif S >= 100000 : print "kichi"
        elif S > 0       : print "syo-kichi"
        else             : print "kyo"
    else:
        print "kyo"