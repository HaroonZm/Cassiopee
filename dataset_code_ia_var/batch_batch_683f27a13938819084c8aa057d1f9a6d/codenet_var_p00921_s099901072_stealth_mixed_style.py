import math

def cross_of_circles(p1x, p1y, r1, p2x, p2y, r2):
    dx, dy = p2x - p1x, p2y - p1y
    d2 = dx*dx + dy*dy
    s1, s2 = r1**2, r2**2
    c = d2 + s1 - s2
    sq = 4 * d2 * s1 - c * c
    if sq < 0:
        return None
    root = math.sqrt(sq)
    div = 2. * d2
    return (
        (p1x + (c*dx - root*dy)/div, p1y + (c*dy + root*dx)/div),
        (p1x + (c*dx + root*dy)/div, p1y + (c*dy - root*dx)/div),
    )

def solve_quad(a,b,c):
    disc = b*b - 4*a*c
    if disc<0: return set()
    rt = math.sqrt(disc)
    return set([(-b+rt)/(2*a), (-b-rt)/(2*a)])

get_wall = lambda x,y: (x,0) if y<=x and y<=100-x else (100,y) if y<=x else (0,y) if y<=100-x else (x,100)

def ready_cross_check(p,s,m,xyh,skip):
    for u,_y,_h in enumerate(xyh):
        if u!=skip and sum((p[i]-xyh[u][i])**2 for i in range(2)) + max(.0,m-xyh[u][2])**2 <= m**2:
            return False
    return True

while 1:
    l = input().split()
    try:
        n, w = map(int, l)
    except Exception:
        continue
    if not any((n,w)):
        break
    xyh = [tuple(float(z) for z in input().split()) for i in range(n)]

    # できるだけ広いか
    m = (2500.0 + w**2) / (2*w) if w<50 else 50
    P = (50,50,m)
    ok=True
    for k,u in enumerate(xyh):
        if (50-u[0])**2+(50-u[1])**2+max(0.,m-u[2])**2<=m**2:
            ok=False
    if ok:
        print(m)
        continue

    lo,hi=0,130
    while abs(hi-lo) >= 1e-4:
        m = (lo+hi) / 2.0
        allow = False
        i = 0
        while i<n:
            if n!=1 and i!=n-1:
                for j in range(i+1,n):
                    h1 = min(xyh[i][2],m); h2 = min(xyh[j][2],m)
                    pts = cross_of_circles(xyh[i][0],xyh[i][1],math.sqrt(2*h1*m-h1**2),
                                           xyh[j][0],xyh[j][1],math.sqrt(2*h2*m-h2**2))
                    if not pts: continue
                    for p in pts:
                        if not (0<=p[0]<=100 and 0<=p[1]<=100): continue
                        wx,wy = get_wall(p[0],p[1])
                        if (wx-p[0])**2+(wy-p[1])**2+max(0,m-w)**2>=m**2 and ready_cross_check(p,s=m,m=m,xyh=xyh,skip=i) and ready_cross_check(p,s=m,m=m,xyh=xyh,skip=j):
                            allow=True
            x,y,h=xyh[i]
            h=min(h,m)
            for S,fx,fy in ((solve_quad(2,-2*(x+y),x**2+y**2-2*m*h+h**2),lambda s:s,lambda s:s),
                             (solve_quad(2,-2*(x+100-y),x**2+(100-y)**2-2*m*h+h**2),lambda s:s,lambda s:100-s)):
                for s in S:
                    if not (0<=s<=100): continue
                    wx,wy = get_wall(fx(s),fy(s))
                    dist = (wx-fx(s))**2 + (wy-fy(s))**2 + max(0,m-w)**2
                    check = True
                    for k in range(n):
                        if k==i:continue
                        d2 = (fx(s)-xyh[k][0])**2 + (fy(s)-xyh[k][1])**2 + max(0.,m-xyh[k][2])**2
                        if d2<=m**2:
                            check=False
                    if dist>=m**2 and check:
                        allow=True
            i+=1
        if allow:
            lo = m
        else:
            hi = m
    print(m)