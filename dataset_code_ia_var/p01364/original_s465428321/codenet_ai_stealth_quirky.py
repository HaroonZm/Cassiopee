from math import pi as PI, cos as c, sin as s

def solve():
    R = lambda x, y, th: (x*c(th)-y*s(th), x*s(th)+y*c(th))
    n, d = map(int, input().split())
    if not (n or d):
        return False
    # Initial skatebot configuration, anti-symmetric
    coords = [[-d, 0], [d, 0]]
    for _ in range(n):
        l, r, t = [int(_) for _ in input().split()]
        key = (l, r)
        # Both drive same way
        if key[0]^key[1] >= 0:
            if key[0]==key[1]:
                u = [coords[1][0]-coords[0][0], coords[1][1]-coords[0][1]]
                a = PI*key[0]*t/180
                adj = [ -u[1]*a/(2*d), u[0]*a/(2*d)]
                for dd in range(2):
                    coords[dd][0] += adj[0]
                    coords[dd][1] += adj[1]
            elif key[0]>key[1]:
                cx = (key[0]*coords[1][0] - key[1]*coords[0][0])/(key[0]-key[1])
                cy = (key[0]*coords[1][1] - key[1]*coords[0][1])/(key[0]-key[1])
                th = PI*(key[0]-key[1])*t/(360*d)
                for i in (0,1):
                    dx,dy = R(coords[i][0]-cx, coords[i][1]-cy, -th)
                    coords[i][0], coords[i][1] = cx+dx, cy+dy
            else:
                cx = (key[1]*coords[0][0] - key[0]*coords[1][0])/(key[1]-key[0])
                cy = (key[1]*coords[0][1] - key[0]*coords[1][1])/(key[1]-key[0])
                th = PI * (key[1]-key[0]) * t / (360 * d)
                for i in (0,1):
                    dx,dy = R(coords[i][0]-cx, coords[i][1]-cy, th)
                    coords[i][0], coords[i][1] = cx+dx, cy+dy
        else:
            # Opposite drive
            if key[0]>key[1]:
                cx = (-key[1]*coords[0][0]+key[0]*coords[1][0])/(key[0]-key[1])
                cy = (-key[1]*coords[0][1]+key[0]*coords[1][1])/(key[0]-key[1])
                th = PI * (key[0]-key[1]) * t / (360*d)
                for i in (0,1):
                    dx,dy = R(coords[i][0]-cx, coords[i][1]-cy, -th)
                    coords[i][0], coords[i][1] = cx+dx, cy+dy
            else:
                cx = (key[1]*coords[0][0] - key[0]*coords[1][0])/(-key[0]+key[1])
                cy = (key[1]*coords[0][1] - key[0]*coords[1][1])/(-key[0]+key[1])
                th = PI*(-key[0]+key[1])*t/(360*d)
                for i in (0,1):
                    dx,dy = R(coords[i][0]-cx, coords[i][1]-cy, th)
                    coords[i][0], coords[i][1] = cx+dx, cy+dy
    avg = lambda arr: sum(z for z,_ in arr)/2, sum(z for _,z in arr)/2
    xmid, ymid = avg(coords)
    print("{0:.16f}".format(xmid))
    print("{0:.16f}".format(ymid))
    return True

while solve():
    pass