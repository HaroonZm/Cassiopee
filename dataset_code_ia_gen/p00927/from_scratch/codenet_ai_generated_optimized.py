import math
import sys
input=sys.stdin.readline

def check_path(d, obs, b, m):
    # Check if a parabolic path with m bounces avoids obstacles
    # m bounces means m+1 segments, each segment length = d/(m+1)
    seg_len = d/(m+1)
    vi = math.sqrt((m+1)*d)
    # Compute initial velocities for each segment
    vix = vi / math.sqrt(1 + m*m)
    viy = m * vix

    # Check obstacles
    # The whole trajectory's parabola is made by concatenation of m+1 identical segments
    # So each segment is from x0 to x0+seg_len with the same parabola turned.
    # After each bounce velocity is reset to initial (vix,viy)
    # So y(x) in segment k (0-based) for x in [x0,x0+seg_len]:
    # y = -x'^2/(2*vix^2) + (viy/vix)*x' where x' = x - x0
    for p,h in obs:
        if p >= d: continue
        k = int(p // seg_len)
        if k > m: k=m
        x0 = k*seg_len
        x_ = p - x0
        y = -(x_**2)/(2*vix**2) + (viy/vix)*x_
        if y < h - 1e-13:
            return False
    return True

d, n, b = map(int,input().split())
obs = [tuple(map(int,input().split())) for _ in range(n)]

low, high = 0.0, 1e9
for _ in range(100):
    mid = (low+high)/2
    ok = False
    for m in range(b+1):
        if check_path(d, obs, b, m):
            # min speed calculation from segment count m:
            # The initial velocity magnitude formula for given m is:
            # From the problem analysis:
            # For segment length l = d/(m+1):
            # minimal vi^2 = (l/2vix)*(l/2viy) * g, with g=1, but simplified:
            # Actually, minimal initial v^2 = ((m+1)*d)
            # but we do binary search on vi, so just check if vi<=mid, so
            # Just use the given mid as initial speed
            # Instead, approximate required minimal vi:
            # vi^2 = vix^2 + viy^2, and viy= m*vix, so vi^2= vix^2*(1+m^2)
            # Also, distance per segment l = 2*vix*viy => l = 2*vix*(m*vix) = 2*m*vix^2
            # So vix^2 = l/(2*m) => but if m=0 then viy=0 and l = 0? But for m=0, l=d and vix^2 = d/2viy -> viy=0, so vix^2 = d/(2*0)? invalid
            # So handle m=0 case: straight shot: vix^2 = d^2/(4*vi_y^2)? Actually, all to binary search, so just simulate trajectories
            if mid >= math.sqrt((m+1)*d):
                # check_path already asserts obstacles not hit
                ok=True
                break
    if ok:
        high = mid
    else:
        low = mid
print('{:.5f}'.format(high))