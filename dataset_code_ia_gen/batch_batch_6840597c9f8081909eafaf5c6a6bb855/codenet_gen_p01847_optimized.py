import sys
def polygon_area(p):
    area=0
    n=len(p)
    for i in range(n):
        x1,y1=p[i]
        x2,y2=p[(i+1)%n]
        area+=x1*y2 - x2*y1
    return abs(area)//2

def inside(p,a,b):
    # vérifie si p est dans la demi-plan définie par la droite a->b (côté gauche)
    # car le polygone est donné en ordre anti-horaire, garder le côté où la normale pointe vers l'extérieur
    return (b[0]-a[0])*(p[1]-a[1]) - (b[1]-a[1])*(p[0]-a[0]) >= 0

def intersect(a1,a2,b1,b2):
    # calcul l'intersection des segments a1a2 et b1b2 du plan (segments rectangulaires donc calcul général)
    dx1=a2[0]-a1[0]
    dy1=a2[1]-a1[1]
    dx2=b2[0]-b1[0]
    dy2=b2[1]-b1[1]
    d=dx1*dy2 - dy1*dx2
    # les polygones convexes et orthogonaux simplifient souvent mais garder la formule générique
    if d==0:
        return None
    t=((b1[0]-a1[0])*dy2 - (b1[1]-a1[1])*dx2)/d
    return (a1[0]+t*dx1,a1[1]+t*dy1)

def clip_polygon(poly,clipper):
    # clip poly par clipper convexe en utilisant Sutherland-Hodgman
    for i in range(len(clipper)):
        new_poly = []
        A=clipper[i]
        B=clipper[(i+1)%len(clipper)]
        for j in range(len(poly)):
            P=poly[j]
            Q=poly[(j+1)%len(poly)]
            inP=inside(P,A,B)
            inQ=inside(Q,A,B)
            if inP and inQ:
                new_poly.append(Q)
            elif inP and not inQ:
                inter=intersect(P,Q,A,B)
                if inter is not None:
                    new_poly.append(inter)
            elif not inP and inQ:
                inter=intersect(P,Q,A,B)
                if inter is not None:
                    new_poly.append(inter)
                new_poly.append(Q)
        poly=new_poly
        if not poly:
            break
    return poly

input=sys.stdin.read().strip().split()
idx=0
while True:
    if idx>=len(input):
        break
    N=int(input[idx])
    idx+=1
    if N==0:
        break
    window=[(int(input[idx+2*i]),int(input[idx+2*i+1])) for i in range(N)]
    idx+=2*N
    curtain=[(int(input[idx+2*i]),int(input[idx+2*i+1])) for i in range(4)]
    idx+=8

    inter=clip_polygon(window,curtain)
    if not inter:
        res=polygon_area(window)
    else:
        res=polygon_area(window)-polygon_area(inter)
    print(res)