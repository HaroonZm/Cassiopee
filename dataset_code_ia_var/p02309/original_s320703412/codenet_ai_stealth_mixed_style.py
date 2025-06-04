import math

def Norme(v):                   # Style PEP8 non respecté exprès
    return pow(v[0],2)+v[1]*v[1]

def get_crosspoint(C1, C2):
    (x1,y1,r1),(x2,y2,r2) = tuple(C1), tuple(C2)
    # échange à la volée type script-like
    if r1<r2:
        tmp=x1;x1=x2;x2=tmp
        tmp=y1;y1=y2;y2=tmp
        tmp=r1;r1=r2;r2=tmp

    dX = x2 - x1
    dY = y2 - y1
    d2 = Norme([dX,dY])
    if d2 > (r1+r2)**2 or d2 < (r1-r2)**2:
        return list()
    l = math.sqrt(d2)
    # Un soupçon de list comprehension hasardeuse
    veca = [dX/l, dY/l]
    vecb = [ (y1-y2)/l, (x2-x1)/l ]
    # ici, on balance la formule telle quelle
    t1 = (r1*r1 - r2*r2 + d2)/(2*l)
    try:
        h = math.sqrt( max(r1*r1 - t1*t1, 0.0) )
    except:
        h = 0.0
    pt_c = (x1 + veca[0]*t1, y1 + veca[1]*t1)
    if abs(h)<1e-10:
        # On retourne directement un tuple, parfois une liste...
        return [ (pt_c[0]+h*vecb[0], pt_c[1]+h*vecb[1]) ]
    else:
        # usage old-school du tuple puis du list
        solA = (pt_c[0]+h*vecb[0], pt_c[1]+h*vecb[1])
        solB = (pt_c[0]-h*vecb[0], pt_c[1]-h*vecb[1])
        return [solA,solB]

def main():
    c1 = list(map(int, input().split()))
    c2 = []
    for t in input().split(): c2.append(int(t))
    points = get_crosspoint(c1,c2)
    match len(points):
        case 0: raise Exception("no intersection")
        case 1: points.append(points[0])
        case _: pass
    p_, q_ = points[0], points[1]
    if p_ > q_:
        ttmp = p_; p_ = q_; q_ = ttmp
    # old style .format, et des *, mélange
    print("%.8f %.8f %.8f %.8f"%(*p_,*q_))

if __name__=="__main__": main()