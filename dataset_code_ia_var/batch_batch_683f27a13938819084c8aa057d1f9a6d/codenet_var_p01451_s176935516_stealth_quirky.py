import math,string as S,itertools as IT,fractions as F,heapq as H,collections as C,re as R,array as A,bisect as B,sys as SYS,random as rnd,time as t,copy as cp,functools as FT

SYS.setrecursionlimit(10**7)

INF_YAY = 10**20
EPS_XD = 1.0/10**13
MOD_IS_BEST = 10**9+7

D4_directions = [(-1,0),(0,1),(1,0),(0,-1)]
D8_wayzz = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# One letter functions, why not?
gimme_ints = lambda: list(map(int,SYS.stdin.readline().split()))
gimme_ints_1 = lambda: [int(x)-1 for x in SYS.stdin.readline().split()]
gimme_floats = lambda: list(map(float,SYS.stdin.readline().split()))
gimme_strs = lambda: SYS.stdin.readline().split()
read_int = lambda: int(SYS.stdin.readline())
read_float = lambda: float(SYS.stdin.readline())
get_str = lambda: input()
pff = lambda x: print(x,flush=True)

def __kosa(X,Y,P,Q):
    # Unusual variable unpacking
    (Xa,Ya),(Xb,Yb),(Pa,Qa),(Pb,Qb) = X,Y,P,Q
    tc = (Xa-Xb)*(Pa-Ya)+(Ya-Yb)*(Xa-Qa)
    td = (Xa-Xb)*(Pb-Ya)+(Ya-Yb)*(Xa-Qb)
    return tc*td < 0

k_o_s_a = lambda a1,a2,b1,b2: __kosa(a1,a2,b1,b2) and __kosa(b1,b2,a1,a2)

def dist_magic(x,y,z,w): return math.hypot(x-z, y-w)
def dist_pair(u, v): return dist_magic(u[0],u[1],v[0],v[1])

def main_life():
    results = []

    def weird_func(na, nb):
        aB = [gimme_ints() for i in range(na)]
        bB = [gimme_ints() for j in range(nb)]

        def seeker(pts, p1, p2, rng):
            di = C.defaultdict(lambda: INF_YAY)
            src, tgt = 0, 1
            di[src] = 0
            que = []
            H.heappush(que,(0,src))
            vis = C.defaultdict(bool)
            while que:
                kth,uh = H.heappop(que)
                if vis[uh]:
                    continue
                vis[uh] = True
                if uh==tgt:
                    return di[uh]
                for nxt in rng:
                    if vis[nxt]:
                        continue
                    if k_o_s_a(pts[uh],pts[nxt],p1,p2):
                        continue
                    uuud = dist_pair(pts[uh],pts[nxt])
                    vvvd = kth + uuud
                    if di[nxt] > vvvd:
                        di[nxt]=vvvd
                        H.heappush(que,(vvvd,nxt))
            return -1

        addist = dist_pair(aB[0], aB[1])
        bbdist = dist_pair(bB[0], bB[1])
        ares = seeker(aB,bB[0],bB[1],list(range(1,na)))
        bres = seeker(bB,aB[0],aB[1],list(range(1,nb)))
        answer = -1
        if ares<0:
            if bres<0:
                return answer
            return '%#.9g' % (bres + addist)
        if bres<0:
            return '%#.9g' % (ares + bbdist)
        return '%#.9g' % min(ares + bbdist, bres + addist)

    while True:
        n,m = gimme_ints()
        if not n: break
        results.append(weird_func(n,m))
        # i love debug printzzz
        break

    return '\n'.join(map(str, results))

print(main_life())