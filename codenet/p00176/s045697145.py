import math
L=[
("black",00,00,00),
("blue",00,00,255),
("lime",00,255,00),
("aqua",00,255,255),
("red",255,00,00),
("fuchsia",255,00,255),
("yellow",255,255,00),
("white",255,255,255)]
while True:
    c=raw_input()
    if c=="0":break
    Rk,Gk,Bk=int(c[1:3],16),int(c[3:5],16),int(c[5:7],16)
    m=10000
    for cl,r,g,b in L:
        t=math.sqrt(pow(r-Rk,2)+pow(g-Gk,2)+pow(b-Bk,2))
        if t<m:
            m=t
            color=cl
    print color