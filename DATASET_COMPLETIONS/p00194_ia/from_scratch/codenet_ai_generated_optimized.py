import sys
import heapq

input=sys.stdin.readline

# Map directions to vector moves (dx, dy)
DIRS={'E':(1,0),'W':(-1,0),'N':(0,-1),'S':(0,1)}
OPPOSITE={'E':'W','W':'E','N':'S','S':'N'}

def to_idx(h,v,m):
    return (ord(h)-97,v-1,m)

def from_idx(x,y,m):
    return chr(x+97),y+1

def neighbors(x,y,m,n):
    res=[]
    if x+1<m: res.append((x+1,y,'E'))
    if x-1>=0: res.append((x-1,y,'W'))
    if y+1<n: res.append((x,y+1,'S'))
    if y-1>=0: res.append((x,y-1,'N'))
    return res

def signal_color(time,k):
    # at t=0, NS green, EW red
    # every k min toggle
    # 0<=time<k NS green
    # k<=time<2k NS red
    # (time//k)%2==0 => NS green, else NS red
    cycle=(time//k)%2
    if cycle==0: return 'NS' # NS green, EW red
    else: return 'EW' # NS red, EW green

while True:
    M,N=map(int,input().split())
    if M==0 and N==0:
        break
    D=int(input())
    ns=int(input())
    sigs={} # (x,y) : k
    for _ in range(ns):
        p,k=input().split()
        h,v= p.split('-')
        x,y,m=to_idx(h,int(v),M)
        sigs[(x,y)]=int(k)
    nc=int(input())
    closed=set()
    for _ in range(nc):
        p1,p2=input().split()
        h1,v1=p1.split('-')
        h2,v2=p2.split('-')
        x1,y1,m1=to_idx(h1,int(v1),M)
        x2,y2,m2=to_idx(h2,int(v2),M)
        a,b= (x1,y1,x2,y2) if (x1,y1)<(x2,y2) else (x2,y2,x1,y1)
        closed.add((a,b))
    nj=int(input())
    jam={} # edge tuple -> dij
    for _ in range(nj):
        p1,p2,d=input().split()
        d=int(d)
        h1,v1=p1.split('-')
        h2,v2=p2.split('-')
        x1,y1,m1=to_idx(h1,int(v1),M)
        x2,y2,m2=to_idx(h2,int(v2),M)
        a,b= (x1,y1,x2,y2) if (x1,y1)<(x2,y2) else (x2,y2,x1,y1)
        jam[(a,b)]=d
    start,end=input().split()
    hs,vs=start.split('-')
    hd,vd=end.split('-')
    sx,sy,m=to_idx(hs,int(vs),M)
    dx,dy,m=to_idx(hd,int(vd),M)

    # Graph is MxN grid by intersections where coordinates: x in [0,M-1], y in [0,N-1]
    # State: position (x,y), direction facing

    # Initial direction: facing East
    # Time limit 100 min

    # At an intersection with signal (k),
    # truck can enter intersection only if signal is green in direction it comes from (or going to? input says
    # red means cannot enter intersection), truck must wait until green if red at arrival time
    # At start, all signals NS green
    # U-turn forbidden

    INF=1<<30
    # dist[x][y][d]: minimal time arrive at (x,y), facing d
    # Directions E=0,W=1,N=2,S=3
    dir_list=['E','W','N','S']
    dist=[[[INF]*4 for _ in range(N)] for __ in range(M)]

    def dir_idx(d):
        return dir_list.index(d)

    hq=[]
    dstart=dir_idx('E')
    dist[sx][sy][dstart]=0
    heapq.heappush(hq,(0,sx,sy,dstart))
    while hq:
        t,x,y,dcur=heapq.heappop(hq)
        if dist[x][y][dcur]<t:
            continue
        if (x,y)==(dx,dy):
            print(t)
            break
        # try move to neighbors except U-turn
        for nx,ny,ndir in neighbors(x,y,M,N):
            if OPPOSITE[ndir]==dir_list[dcur]:
                continue
            # check closed road
            a,b= (x,y,nx,ny) if (x,y)<(nx,ny) else (nx,ny,x,y)
            if (a,b) in closed:
                continue
            # edge cost
            extra=jam.get((a,b),0)
            cost=D+extra
            nt=t+cost
            # check signal at arrival intersection (nx,ny) if signal exist
            if (nx,ny) in sigs:
                k=sigs[(nx,ny)]
                tm=nt% (2*k)
                # signal states repeat 2k min
                # When truck arrive at intersection, entrance allowed only if signal green on direction of travel,
                # that is, the direction of road i.e. the intersection signal cycles between NS green & EW green
                # we need to check if direction ndir is green at time nt.
                # if ndir in NS ('N' or 'S') then signal must show NS green else red
                # Similarly for EW (E or W)
                ndir_group = 'NS' if ndir in 'NS' else 'EW'
                cur_color='NS' if tm<k else 'EW'
                if ndir_group != cur_color:
                    # wait until green
                    wait = (k - (tm % k)) % k
                    nt+=wait
            ndir_i=dir_idx(ndir)
            if dist[nx][ny][ndir_i]>nt:
                dist[nx][ny][ndir_i]=nt
                heapq.heappush(hq,(nt,nx,ny,ndir_i))