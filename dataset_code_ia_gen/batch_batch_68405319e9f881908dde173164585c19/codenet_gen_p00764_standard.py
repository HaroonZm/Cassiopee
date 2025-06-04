import sys
import math

def intersect_points(x1,y1,r1,x2,y2,r2):
    d=math.hypot(x2-x1,y2-y1)
    a=(r1*r1 - r2*r2 + d*d)/(2*d)
    h=math.sqrt(r1*r1 - a*a)
    xm=x1 + a*(x2 - x1)/d
    ym=y1 + a*(y2 - y1)/d
    xs1 = xm + h*(y2 - y1)/d
    ys1 = ym - h*(x2 - x1)/d
    xs2 = xm - h*(y2 - y1)/d
    ys2 = ym + h*(x2 - x1)/d
    return (xs1,ys1),(xs2,ys2)

def arc_length(r,theta):
    return r*theta

def angle_between(center, p):
    return math.atan2(p[1]-center[1], p[0]-center[0])

def shortest_arc(r,a1,a2):
    diff=abs(a1 - a2)
    return r*min(diff,2*math.pi - diff)

def main():
    input=sys.stdin.read().strip().split()
    pos=0
    while True:
        if pos>=len(input):
            break
        n=int(input[pos]); pos+=1
        if n==0:
            break
        circles=[]
        for _ in range(n):
            x=int(input[pos]); y=int(input[pos+1]); r=int(input[pos+2])
            pos+=3
            circles.append((x,y,r))
        points=[[] for _ in range(n)]
        # first and last circle centers as nodes
        points[0].append(('center',circles[0][0],circles[0][1]))
        points[-1].append(('center',circles[-1][0],circles[-1][1]))
        # compute intersection points between adjacent circles
        inter_points = []
        for i in range(n-1):
            c1=circles[i]; c2=circles[i+1]
            p1,p2=intersect_points(*c1,*c2)
            points[i].append(('int',p1[0],p1[1],i+1,len(points[i+1])))
            points[i].append(('int',p2[0],p2[1],i+1,len(points[i+1])+1))
            points[i+1].append(('int',p1[0],p1[1],i,len(points[i])-2))
            points[i+1].append(('int',p2[0],p2[1],i,len(points[i])-1))
        # build graph
        # each node: (circle_index,node_index)
        # edges inside each circle: arcs between points ordered on circle
        # edges between circles: intersection points connected
        graph = {}
        def add_edge(a,b,dist):
            if a not in graph:
                graph[a]={}
            graph[a][b]=dist
        for i in range(n):
            pts=points[i]
            center=circles[i][:2]
            r=circles[i][2]
            # sort points by angle around center
            angles=[]
            for idx,p in enumerate(pts):
                if p[0]=='center':
                    ang = 0
                else:
                    ang=angle_between(center,p[1:3])
                angles.append((ang,idx,p))
            angles.sort(key=lambda x:x[0])
            m=len(angles)
            # add arcs between adjacent points on circle (both directions)
            for j in range(m):
                a1,a2=angles[j],angles[(j+1)%m]
                idx1,idx2=a1[1],a2[1]
                p1,p2=a1[2],a2[2]
                if p1[0]=='center' and p2[0]=='center':
                    dist=math.hypot(center[0]-center[0],center[1]-center[1])
                else:
                    dist=shortest_arc(r,a1[0],a2[0])
                add_edge((i,idx1),(i,idx2),dist)
                add_edge((i,idx2),(i,idx1),dist)
        # add zero-length edges between same intersection points in adjacent circles
        for i in range(n-1):
            cpoints_1=points[i]
            cpoints_2=points[i+1]
            for idx1,p1 in enumerate(cpoints_1):
                if p1[0]!='int':
                    continue
                for idx2,p2 in enumerate(cpoints_2):
                    if p2[0]!='int':
                        continue
                    same_points=abs(p1[1]-p2[1])<1e-9 and abs(p1[2]-p2[2])<1e-9
                    if same_points:
                        add_edge((i,idx1),(i+1,idx2),0.0)
                        add_edge((i+1,idx2),(i,idx1),0.0)
        start=(0,0)
        end=(n-1,0)
        # Dijkstra
        import heapq
        dist={}
        dist[start]=0.0
        heap=[(0.0,start)]
        while heap:
            cd,u = heapq.heappop(heap)
            if u==end:
                print(f"{cd:.6f}")
                break
            if dist[u]<cd:
                continue
            for v in graph.get(u,{}):
                nd=cd+graph[u][v]
                if v not in dist or nd<dist[v]:
                    dist[v]=nd
                    heapq.heappush(heap,(nd,v))

if __name__=="__main__":
    main()