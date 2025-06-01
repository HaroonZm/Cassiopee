import sys
import math

def in_fan(x, y, r, theta, angle, radius):
    dx, dy = x, y
    dist = math.hypot(dx, dy)
    if dist > radius + 1e-9:
        return False
    if dist < 1e-9:
        return True
    angle_p = math.degrees(math.atan2(dy, dx)) % 360
    diff = min((angle_p - theta) % 360, (theta - angle_p) % 360)
    return diff <= angle / 2 + 1e-9

input = sys.stdin.readline

while True:
    H, R = map(int, input().split())
    if H == 0 and R == 0:
        break
    houses = [tuple(map(int, input().split())) for _ in range(H)]
    U, M, S, du, dm, ds = map(int, input().split())
    ume = [tuple(map(int, input().split())) for _ in range(U)]
    momo = [tuple(map(int, input().split())) for _ in range(M)]
    sakura = [tuple(map(int, input().split())) for _ in range(S)]
    winds = [tuple(map(int, input().split())) for _ in range(R)]

    # Precompute angles and distances for all flowers and houses
    # For each house and each flower set, store if house is in fan of flower type for given wind
    # We check per day

    # For efficiency, precompute a list of flower info: (x,y, angle, radius)
    # radius is wind strength a for that day, varies per day
    # so just store coordinates per flower

    # The main check per day:
    # For each house:
    #  Check if in our ume fan (angle du, radius a, direction w)
    #  Check if in other ume fans (du, a, w)
    #  And in momo fans (dm, a, w)
    #  And sakura fans (ds, a, w)
    # Condition: in our ume fan AND in none of other flowers fans

    # Since our ume is at origin (0,0)
    # Our ume fan is always at origin with du

    counts = [0]*H
    for w,a in winds:
        # Check for each house
        # Our ume fan
        def is_our_ume(hx, hy):
            return in_fan(hx, hy, du, w, du, a)
        # Other ume fans
        def in_any_other_ume(hx, hy):
            for x,y in ume:
                if in_fan(hx - x, hy - y, du, w, du, a):
                    return True
            return False
        def in_any_momo(hx, hy):
            for x,y in momo:
                if in_fan(hx - x, hy - y, dm, w, dm, a):
                    return True
            return False
        def in_any_sakura(hx, hy):
            for x,y in sakura:
                if in_fan(hx - x, hy - y, ds, w, ds, a):
                    return True
            return False

        for i,(hx, hy) in enumerate(houses):
            if is_our_ume(hx, hy) and not (in_any_other_ume(hx, hy) or in_any_momo(hx, hy) or in_any_sakura(hx, hy)):
                counts[i]+=1

    max_count = max(counts)
    if max_count == 0:
        print("NA")
    else:
        res = [str(i+1) for i,c in enumerate(counts) if c == max_count]
        print(" ".join(res))