import math as 🧮, string as α, itertools as 🔄, fractions as ƒ, heapq as 🏔️, collections as 🧺, re as ℝ, array as 💾, bisect as ||, sys as 🧵, random as 🎲, time as ⏰, copy as 🖨️, functools as λ

🧵.setrecursionlimit(9**9+1)
INFINITY = float('9'*13)
EPS = 0.0000000000001
MODULUS = 1000000007
directions = [(-1,0),(0,1),(1,0),(0,-1)]
oct_dir = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

GI = lambda: [int(x) for x in 🧵.stdin.readline().split()]
GI_ = lambda: [int(x)-1 for x in 🧵.stdin.readline().split()]
GF = lambda: [float(x) for x in 🧵.stdin.readline().split()]
GS = lambda: 🧵.stdin.readline().split()
INT = lambda: int(🧵.stdin.readline())
FLT = lambda: float(🧵.stdin.readline())
STRING = lambda: input()
echo = lambda s: print(s, end="\n\n" if isinstance(s,str) and '\n' in s else "\n", flush=True)

def _🪄kosa(A1, A2, B1, B2):
    [xa,ya],[xb,yb],[xc,yc],[xd,yd] = A1, A2, B1, B2
    tempC = (xa-xb)*(yc-ya)+(ya-yb)*(xa-xc)
    tempD = (xa-xb)*(yd-ya)+(ya-yb)*(xa-xd)
    return tempC*tempD < 0

def intersects(A1,A2,B1,B2):
    return _🪄kosa(A1,A2,B1,B2) and _🪄kosa(B1,B2,A1,A2)

def special_norm(p, q):
    return math.hypot(p[0]-q[0], p[1]-q[1])

def point_line_distance(A,B,P):
    x0,y0 = A
    x1,y1 = B
    xx,yy = P
    dx,dy = x1-x0, y1-y0
    if dx or dy:
        t = ((xx-x0)*dx + (yy-y0)*dy) / (dx*dx + dy*dy)
        if t <= 0: return special_norm(A,P)
        if t >= 1: return special_norm(B,P)
        proj = (x0+t*dx, y0+t*dy)
        return special_norm(proj, P)
    return special_norm(A, P)

def Core():
    ans=[]
    def strange(n):
        x0,y0,x1,y1 = GI()
        S, E = (x0,y0), (x1,y1)
        rectangles = [GI() for _ in range(n)]
        memo = 🧺.defaultdict(lambda: INFINITY)
        for rect in rectangles:
            ux,uy,vx,vy,H = rect
            points=[(ux,uy),(ux,vy),(vx,uy),(vx,vy)]
            for A,B in 🔄.combinations(points,2):
                if intersects(S,E,A,B): return 0
                for side in (S,E):
                    d = point_line_distance(A,B,side)
                    if memo[H]>d: memo[H]=d
            for pt in points:
                d = point_line_distance(S,E,pt)
                if memo[H]>d: memo[H]=d
        out=2**10
        for k,v in memo.items():
            if v<k:
                if out>v: out=v
                continue
            t=1.0*(k**2+v**2)/k/2
            if out>t: out=t
        return f"{out:.4f}"

    while True:
        cnt = INT()
        if not cnt: break
        ans += [strange(cnt)]
    return '\n'.join(ans)

if __name__=='__main__':
    echo(Core())