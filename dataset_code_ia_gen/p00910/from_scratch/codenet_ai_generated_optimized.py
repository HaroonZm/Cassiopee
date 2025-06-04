import sys
import math

def dist_sq(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

def segment_intersects_balloon(S,E,r,C):
    # Check if segment SE intersects sphere with center C and radius r
    # Vector SE
    sx,sy,sz=E[0]-S[0],E[1]-S[1],E[2]-S[2]
    # Vector SC
    cx,cy,cz=C[0]-S[0],C[1]-S[1],C[2]-S[2]
    se_len_sq = sx*sx+sy*sy+sz*sz
    proj = sx*cx+sy*cy+sz*cz # projection length of SC on SE
    if proj<=0:
        # Closest point is S
        d_sq = (C[0]-S[0])**2+(C[1]-S[1])**2+(C[2]-S[2])**2
        return d_sq<r*r
    if proj>=se_len_sq:
        # Closest point is E
        d_sq = (C[0]-E[0])**2+(C[1]-E[1])**2+(C[2]-E[2])**2
        return d_sq<r*r
    # Closest point is inside segment
    closest_x = S[0]+sx*proj/se_len_sq
    closest_y = S[1]+sy*proj/se_len_sq
    closest_z = S[2]+sz*proj/se_len_sq
    d_sq = (C[0]-closest_x)**2+(C[1]-closest_y)**2+(C[2]-closest_z)**2
    return d_sq<r*r

def main():
    input=sys.stdin.read().strip().split()
    idx=0
    out=[]
    while True:
        if idx>=len(input):
            break
        N,M,R= map(int,input[idx:idx+3])
        idx+=3
        if N==0 and M==0 and R==0:
            break
        balloons=[]
        for _ in range(N):
            x,y,z,r= map(int,input[idx:idx+4])
            idx+=4
            balloons.append((x,y,z,r))
        lights=[]
        for _ in range(M):
            x,y,z,b= map(int,input[idx:idx+4])
            idx+=4
            lights.append((x,y,z,b))
        Ex,Ey,Ez= map(int,input[idx:idx+3])
        idx+=3
        E=(Ex,Ey,Ez)
        # Compute for each light source its intensity at E
        lights_intensity=[]
        for (x,y,z,b) in lights:
            d2 = dist_sq((x,y,z),E)
            intensity=b/d2
            lights_intensity.append(intensity)
        # For each light, find which balloons block it
        # Array blocked_by_light: for each light index, store set of balloon indices that block it
        blocked_by_light = [set() for _ in range(M)]
        # Also for each balloon, store which lights it blocks
        lights_blocking_balloon = [set() for _ in range(N)]
        # Precompute to accelerate search about which balloons block each light
        for i,(lx,ly,lz,b) in enumerate(lights):
            for j,(cx,cy,cz,r) in enumerate(balloons):
                if segment_intersects_balloon((lx,ly,lz), E, r, (cx,cy,cz)):
                    blocked_by_light[i].add(j)
                    lights_blocking_balloon[j].add(i)
        # Determine which lights are initially visible (no balloon blocks them)
        visible = [len(blocked_by_light[i])==0 for i in range(M)]
        total_intensity = 0.0
        for i,v in enumerate(visible):
            if v:
                total_intensity+=lights_intensity[i]
        # If we can remove no balloons, output total_intensity
        if R==0:
            out.append(str(total_intensity))
            continue
        # If we can remove >= balloons count, all become visible
        if R>=N:
            out.append(str(sum(lights_intensity)))
            continue
        # For each balloon, calculate the gain in total illumination if removed
        # gain is sum of intensities of lights where this balloon is the only blocker
        gains = [0.0]*N
        # For each light that is not visible (blocked), count blockers
        num_blockers = [len(blocked_by_light[i]) for i in range(M)]
        # For each balloon
        for j in range(N):
            gain = 0.0
            for i in lights_blocking_balloon[j]:
                # Check if balloon j is the only balloon blocking light i
                if num_blockers[i]==1:
                    gain+=lights_intensity[i]
            gains[j]=gain
        # Greedy remove balloons with highest gains, update state accordingly
        removed = set()
        import heapq
        # Use max heap with (-gain, balloon index)
        heap = [(-gains[j], j) for j in range(N)]
        heapq.heapify(heap)
        # To update gains dynamically, store for each balloon which lights it blocks
        # and for each light, which balloons block it
        while R>0 and heap:
            g, bidx = heapq.heappop(heap)
            if bidx in removed:
                continue
            # Check current gain
            # Recompute current gain to avoid stale heap elements
            cur_gain=0.0
            for li in lights_blocking_balloon[bidx]:
                if li<0 or li>=M:
                    continue
                if num_blockers[li]==1:
                    cur_gain+=lights_intensity[li]
            if -g != cur_gain:
                heapq.heappush(heap,(-cur_gain,bidx))
                continue
            if cur_gain==0.0:
                break
            # Remove balloon bidx
            removed.add(bidx)
            R-=1
            # Update affected lights blockers
            for li in lights_blocking_balloon[bidx]:
                if li<0 or li>=M:
                    continue
                old_nb = num_blockers[li]
                if old_nb==0:
                    continue
                num_blockers[li]-=1
                if num_blockers[li]==0:
                    total_intensity+=lights_intensity[li]
                if num_blockers[li]<0:
                    num_blockers[li]=0
            # No need to update gains of all balloons fully, rely on lazy update in heap
        out.append(str(total_intensity))
    print('\n'.join(out))

if __name__=="__main__":
    main()