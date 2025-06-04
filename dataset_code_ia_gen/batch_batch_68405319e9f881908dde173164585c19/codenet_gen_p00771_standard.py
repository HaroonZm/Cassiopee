import sys
import math

def can_place(n, anchors, ropes, h):
    points = [(0,0,h) for _ in range(n)]
    # For each rope, the balloon point must satisfy distance to anchor <= rope length
    for i in range(n):
        x,y,l = anchors[i][0], anchors[i][1], ropes[i]
        dx = x - 0
        dy = y - 0
        # Horizontal dist from origin to anchor
        dist_xy = math.sqrt(dx*dx + dy*dy)
        # At height h, distance from anchor must <= rope length
        # Distance from (x,y,0) to (0,0,h) = sqrt(x² + y² + h²)
        if math.sqrt((x)**2+(y)**2 + h*h) > l + 1e-12:
            return False
    # Now check for rope crossing
    # Each rope is modeled as segment from anchor (x,y,0) to balloon (0,0,h)
    # For no crossing: For any two ropes, the projection to xy plane must not cross
    # because the ropes are straight lines 3D from anchor to balloon above origin
    # We check if the lines cross at heights between 0 and h
    # Due to vertical straightness and common balloon point, no crossing if anchors lines do not cross
    # Projecting anchors to xy plane, and balloon to (0,0)
    # So in 2D, edges are from anchor points to origin.
    # No crossing means segments from anchors to origin do not intersect except at origin
    # This is equivalent to checking if any pair of anchors make segments from anchor to origin intersect
    # except at origin.
    anchor_points = [(a[0],a[1]) for a in anchors]
    for i in range(n):
        for j in range(i+1,n):
            # segments: anchor i to origin and anchor j to origin
            # If they only intersect at origin, that's fine.
            # Otherwise crossing means there is intersection between these two segments other than origin
            ai = anchor_points[i]
            aj = anchor_points[j]
            # If anchors are colinear with origin, check if segments overlap beyond origin:
            # Colinear check:
            cross = ai[0]*aj[1] - ai[1]*aj[0]
            if abs(cross) < 1e-14:
                # colinear
                # Check if anchors are on opposite sides of origin:
                dot = ai[0]*aj[0]+ai[1]*aj[1]
                if dot < 0:
                    # cross at origin only, okay
                    continue
                # Else check distance
                if (ai[0]*ai[0]+ai[1]*ai[1]) < (aj[0]*aj[0]+aj[1]*aj[1]):
                    # segments overlap => crossing
                    return False
                # Else no crossing
            else:
                # Check intersection of segments from anchor to origin except at origin
                # Parametric lines L1: origin + t*(-ai), t in [0,1]
                # L2: origin + s*(-aj), s in [0,1]
                # Find if exists t,s in (0,1) such that L1(t)=L2(s)
                denom = aj[0]*ai[1] - aj[1]*ai[0]
                if abs(denom) < 1e-14:
                    continue
                t = (aj[0]*0 - aj[0]*aj[1]) / denom if denom != 0 else 0
                # Alternative: Check intersection of two segments from two points to origin is handled by cross
                # Here simpler to check if segments intersect other than origin means segments cross
                # For origin and two anchors, if the segments cross, their anchors are in different angles and segments intersect at origin only
                # So no crossing here, continue
                pass
    return True

def main():
    input = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input):
            break
        n = int(input[idx])
        idx += 1
        if n == 0:
            break
        anchors = []
        ropes = []
        for _ in range(n):
            x,y,l = map(int, input[idx].split())
            idx += 1
            anchors.append((x,y))
            ropes.append(l)
        low = 0.0
        high = 300.0
        for _ in range(100):
            mid = (low+high)/2
            if can_place(n, anchors, ropes, mid):
                low = mid
            else:
                high = mid
        print("%.7f"%low)

if __name__=="__main__":
    main()