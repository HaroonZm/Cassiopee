import sys
import math
from collections import defaultdict, deque

def length(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

def dot(u,v):
    return u[0]*v[0]+u[1]*v[1]

def vec(a,b):
    return (b[0]-a[0], b[1]-a[1])

def angle_cos(a,b,c): # cos angle at b between ba and bc
    ba = vec(b,a)
    bc = vec(b,c)
    n1 = math.hypot(*ba)
    n2 = math.hypot(*bc)
    if n1==0 or n2==0:
        return 1
    return dot(ba,bc)/(n1*n2)

def readints():
    return map(int,sys.stdin.readline().split())

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        n=line.strip()
        if n=='0': break
        n=int(n)
        xs,ys= map(int,sys.stdin.readline().split())
        xg,yg= map(int,sys.stdin.readline().split())
        segs=[]
        for _ in range(n):
            x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
            segs.append(((x1,y1),(x2,y2)))
        points = set()
        for s in segs:
            points.add(s[0])
            points.add(s[1])
        # identify street segments: those connected to multiple segments at endpoints
        adjacency_count=defaultdict(int)
        for s in segs:
            adjacency_count[s[0]]+=1
            adjacency_count[s[1]]+=1
        # categorize edges as street or sign:
        # streets: endpoints have adjacency_count>=1 (all have at least 1)
        # signs: one endpoint touches exactly one street, other is open.
        # We can define that a street segment is one where both endpoints connect at least 1 segment
        # Signs connect to a node of degree 1 only at one endpoint, other is unique to signs
        
        # Determine which segments are streets by grouping connected graphs without considering signs
        # Actually, problem states streets are the segments that connect point to point with possibly multiple connections
        # Signs have one endpoint that touches one and only one line segment representing a street, other open.

        # Build maps of endpoints to segments
        endpoint_seg = defaultdict(list)
        for i,(p1,p2) in enumerate(segs):
            endpoint_seg[p1].append(i)
            endpoint_seg[p2].append(i)
        # Build street graph:
        # street segments are those where both endpoints have degree>1 or connected to more than one segment (means intersection)
        # signs are those attached to endpoint with degree==1 at one side and open other endpoint (degree==0 or no connection)
        
        # Determine which segments are signs: if one endpoint is attached to exactly one street, other endpoint only connected to this segment
        # But to know street segments we need to exclude signs.
        # We'll assume streets form a graph with nodes at intersection points where a point connects 2 or more street segments
        # Signs connect to exactly one street segment endpoint and one open endpoint.

        # Build initial graph ignoring directions
        graph = defaultdict(list)
        # We'll label each segment as street or sign:
        street_segments = set()
        sign_segments = set()
        point_degree = defaultdict(int)

        # First, count how many segments per point
        seg_count_per_point=defaultdict(int)
        for p in points:
            seg_count_per_point[p]=len(endpoint_seg[p])
        # From problem: signs touch only one street, other end open
        # So signs are segments with one endpoint degree =1 and other endpoint degree=0 or no connections
        # Actually degree=0 impossible, as they are endpoints so unreachable? But problem says
        for i,(p1,p2) in enumerate(segs):
            d1 = seg_count_per_point[p1]
            d2 = seg_count_per_point[p2]
            # Condition for sign:
            # one endpoint touches only one street segment (=1)
            # other endpoint touches no street (0) or unique to this sign segment only (likely 1 too but only for this sign)
            # So sign segments have one endpoint with degree=1 and other endpoint with degree=1 but connected only to the sign
            # To find this, we check if one endpoint appears only once in all segments (only this sign)
            # count number of segments involving p1 and p2
            # If one endpoint connected to one segment (the sign itself), and the other endpoint connected to another segment (street)
            # Then it's sign
            if d1==1 and d2==1:
                # Check how many segments each endpoint involved: if endpoint involved in only this segment?
                # Both 1 here, but maybe one is sign, other street
                # We check if either endpoint involved in multiple segments is street
                # Let's count how many segments each endpoint connected to, and which segments
                # The other endpoint connected to at least one street segment.
                # We'll defer this, so far treat as sign candidate.
                sign_segments.add(i)
            else:
                street_segments.add(i)
        # There could be signs with endpoints both degree=1, but then to identify which is hanging endpoint:
        # Reassign sign segments correctly:
        # Actually, problem says: end point of a sign touches one and only one street segment and other endpoint is open.
        # So in sign segment: exactly one endpoint p has degree>1 or connected to a street segment, the other endpoint connected to no other segments besides the sign itself.

        def is_sign(i):
            p1,p2=segs[i]
            d1 = seg_count_per_point[p1]
            d2 = seg_count_per_point[p2]
            # Count how many street segments connected to p1 and p2
            street_p1 = 0
            for sidx in endpoint_seg[p1]:
                if sidx==i:continue
                if sidx in street_segments:
                    street_p1+=1
            street_p2 = 0
            for sidx in endpoint_seg[p2]:
                if sidx==i:continue
                if sidx in street_segments:
                    street_p2+=1
            # One endpoint must touch exactly one street segment (street count=1), other None
            if (street_p1==1 and street_p2==0) or (street_p2==1 and street_p1==0):
                return True
            return False

        # Refine sign/street sets
        street_segments = set()
        for i in range(n):
            if is_sign(i):
                sign_segments.add(i)
            else:
                street_segments.add(i)

        # Build graph over points (intersection of streets) with edges oriented according to street direction rules
        # Construct undirected graph of streets first
        graph_undirected=defaultdict(set)
        for i in street_segments:
            p1,p2=segs[i]
            graph_undirected[p1].add(p2)
            graph_undirected[p2].add(p1)

        # Intersection points: points with degree >=2 in street graph
        intersection_points = set()
        deg_street = defaultdict(int)
        for p in graph_undirected:
            deg_street[p]=len(graph_undirected[p])
            if deg_street[p]>=2:
                intersection_points.add(p)

        # We need to make a directed graph considering signs' forbidden directions.
        # Signs restrict movement from obtuse side to acute side at a point where a sign touches a street.
        # At the endpoint where sign touches a street, label angles between sign and street.
        # Cars may not move from the obtuse angle side to acute side.
        # Special rectangular (right angle) => no movement either direction.

        # For each sign:
        # Let sign endpoints be (S,E), S connected to street node P, E open
        # The point where sign touches street is S (or E), find which is connected to exactly one street segment.

        # For each sign, determine orientation:
        # Calculate the angles between sign (segment) and adjacent street (segment) at the touching point
        # Then restrict direction accordingly.

        # We build an initial directed graph allowing all edges both directions between street nodes:
        graph_directed=defaultdict(list)
        edge_len = dict()
        for i in street_segments:
            p1,p2=segs[i]
            d=length(p1,p2)
            graph_directed[p1].append((p2,d))
            graph_directed[p2].append((p1,d))
            edge_len[(p1,p2)]=d
            edge_len[(p2,p1)]=d

        # For each sign, impose restrictions
        # find touching point = endpoint connected to street
        for i in sign_segments:
            s,e = segs[i]
            # determine touching endpoint:
            # the endpoint that connects to a street
            # The other endpoint is open (connected only to this sign)
            # check connections in street_segments involving s and e
            s_street_count=0
            e_street_count=0
            for si in endpoint_seg[s]:
                if si in street_segments:
                    s_street_count+=1
            for si in endpoint_seg[e]:
                if si in street_segments:
                    e_street_count+=1
            if s_street_count==1 and e_street_count==0:
                touch = s
                open_end = e
            elif e_street_count==1 and s_street_count==0:
                touch = e
                open_end = s
            else:
                # not matching problem condition
                continue
            # The unique street segment attached at touch is:
            street_seg_idx = -1
            for si in endpoint_seg[touch]:
                if si in street_segments:
                    street_seg_idx=si
                    break
            if street_seg_idx==-1:
                continue
            # The street segment:
            sp1,sp2=segs[street_seg_idx]
            # At touch point, find other endpoint of street segment: opposite point
            if sp1==touch:
                street_other = sp2
            else:
                street_other = sp1
            # Calculate angle at touch between sign and street
            # vectors: sign from touch to open_end, street from touch to street_other
            v_sign = vec(touch, open_end)
            v_street = vec(touch, street_other)
            # angle cosine:
            c = dot(v_sign, v_street)/(math.hypot(*v_sign)*math.hypot(*v_street))
            # Due to float precision, clip c to [-1,1]
            c=max(-1,min(1,c))
            # angle = arccos(c)
            # Determine sign constraints:
            # If angle is right approx cos=0 => no movement either direction
            # If angle < 90 (cos>0) acute angle
            # If angle >90 (cos<0) obtuse angle
            # Movement forbids from obtuse to acute side at point. 
            # So from side formed by street at obtuse angle to side of acute angle is forbidden.
            # The obtuse side is on side with angle >90.
            # The acute side is with angle <90.
            # Because sign touches street at a point, a node, we see street/node edges and limit edges accordingly.
            # This is local direction restriction between node touch and street_other node(s)
            
            # Interpret:
            # For the node touch, the car cannot move from side of obtuse angle to side of acute angle
            # The two street edges adjacent at touch: only one street edge or possibly multiple, how to handle?
            # As per problem, at a point where sign touches street, movement from obtuse angle side to acute angle side is forbidden.
            # There is only one street segment connected at touch in the sign's touching segment,
            # so the forbidden movement is depending on direction between touch and street_other nodes.

            # To find orientation of allowed and forbidden direction:
            # We consider that "the obtuse side" is corresponding to the direction vertex oppsite to the acute side
            # The direction from the sign point towards the street_other is on one side, direction from street_other to touch is opposite side
            # So direction from obtuse to acute side means: moving from which node to which node
            # The obtuse side is from the other endpoint of street segment to touch or from touch to other endpoint?

            # Actually, problem example "BF" - car cannot move from obtuse angle side to acute angle side at the node B
            # So forbidden direction is from node on obtuse side to node on acute side

            # So we consider the edge between touch and street_other, orient:
            # Determine position of obtuse and acute side around the node
            # The edge between touch and street_other in both directions possibly allowed, restrict direction depending on sign

            # We thus forbid movement from obtuse angle side to acute angle side of the point touch on street edge between touch and street_other
            
            # We distinguish the two ends of the edge (touch and street_other):
            # At node touch, angle is obtuse or acute between sign and street edge
            # From obtuse side to acute side is forbidden => must remove directed edge from node on obtuse side to node on acute side

            # We need to decide which node correspond to the obtuse side and which to acute side.
            # By default, direction from touch to street_other is out from touch, from street_other to touch is in opposite direction.
            # Angle computed at touch.
            # So angle between sign and street at touch is c.
            # If c>0, angle acute, obtuse side is opposite direction (street_other)
            # If c<0, angle obtuse, obtuse side is touch

            # So if angle is acute(c>0), forbidden movement is from street_other (obtuse side) to touch (acute side)
            # If angle is obtuse(c<0), forbidden movement is from touch (obtuse side) to street_other (acute side)
            # If angle right (~0), forbidden both directions

            # Implement accordingly
            eps = 1e-14
            if abs(c)<eps:
                # right angle
                # forbid both directions between touch and street_other
                if (touch,street_other) in edge_len:
                    graph_directed[touch] = [(w,d) for w,d in graph_directed[touch] if w!=street_other]
                if (street_other,touch) in edge_len:
                    graph_directed[street_other] = [(w,d) for w,d in graph_directed[street_other] if w!=touch]
            elif c>0:
                # acute
                # forbid movement from obtuse side to acute side
                # obtuse side is street_other, acute side touch
                # forbid street_other->touch
                if street_other in [w for w,d in graph_directed]:
                    graph_directed[street_other] = [(w,d) for w,d in graph_directed[street_other] if w!=touch]
            else:
                # obtuse
                # forbid touch->street_other
                graph_directed[touch] = [(w,d) for w,d in graph_directed[touch] if w!=street_other]

        # Some points have only one street or are endpoints, to allow movement:
        # but problem states cars may not move from P to M or M to P in map where signs N,O forbid passing through them; this is modeled.
        # After applying all sign restrictions, graph_directed is ready.

        # Start and Goal points:
        start = (xs,ys)
        goal = (xg,yg)

        # If start or goal not in points or not on street
        if start not in points or goal not in points:
            print(-1)
            print(0)
            continue

        # Dijkstra on graph_directed
        dist = {p:math.inf for p in points}
        prev = {}
        dist[start]=0
        import heapq
        heap = [(0,start)]
        while heap:
            cd,u = heapq.heappop(heap)
            if cd>dist[u]:
                continue
            if u==goal:
                break
            for w,dw in graph_directed.get(u,[]):
                nd = cd+dw
                if nd<dist[w]:
                    dist[w]=nd
                    prev[w]=u
                    heapq.heappush(heap,(nd,w))
        if dist[goal]==math.inf:
            print(-1)
            print(0)
            continue

        # reconstruct path
        path=[]
        cur=goal
        while cur!=start:
            path.append(cur)
            cur=prev[cur]
        path.append(start)
        path.reverse()

        # print intersection points on path:
        # street intersection point: point where at least two street segments meet
        # these are points with degree >=2 in street graph
        for p in path:
            if p in intersection_points:
                print(p[0],p[1])
        print(0)

if __name__=="__main__":
    main()