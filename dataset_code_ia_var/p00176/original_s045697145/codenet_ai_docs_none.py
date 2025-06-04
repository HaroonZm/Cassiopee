import math
L=[
("black",0,0,0),
("blue",0,0,255),
("lime",0,255,0),
("aqua",0,255,255),
("red",255,0,0),
("fuchsia",255,0,255),
("yellow",255,255,0),
("white",255,255,255)]
while True:
    c=raw_input()
    if c=="0":break
    Rk,Gk,Bk=int(c[1:3],16),int(c[3:5],16),int(c[5:7],16)
    m=10000
    for cl,r,g,b in L:
        t=math.sqrt((r-Rk)**2+(g-Gk)**2+(b-Bk)**2)
        if t<m:
            m=t
            color=cl
    print color