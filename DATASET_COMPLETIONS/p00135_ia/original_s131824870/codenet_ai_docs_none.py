n=int(raw_input())
for i in range(n):
    t=[int(x) for x in raw_input().split(':')]
    longdeg=t[1]*360/60.
    shortdeg=t[0]*360/12.+t[1]*30/60.
    (longdeg,shortdeg)=(max(longdeg,shortdeg),min(longdeg,shortdeg))
    dist=min(longdeg-shortdeg,360-(longdeg-shortdeg))
    if dist<30:
        print 'alert'
    elif dist>=90:
        print 'safe'
    else:
        print 'warning'