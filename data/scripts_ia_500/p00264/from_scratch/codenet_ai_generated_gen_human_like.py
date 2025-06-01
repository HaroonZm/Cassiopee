import sys
import math

def in_sector(px, py, radius, center_angle, half_angle):
    dist = math.hypot(px, py)
    if dist > radius:
        return False
    angle = math.degrees(math.atan2(py, px)) % 360
    c1 = (angle - center_angle) % 360
    c2 = (center_angle - angle) % 360
    return c1 <= half_angle or c2 <= half_angle

for line in sys.stdin:
    if not line.strip():
        continue
    H, R = map(int, line.split())
    if H == 0 and R == 0:
        break
    houses = [tuple(map(int, sys.stdin.readline().split())) for _ in range(H)]
    U, M, S, du, dm, ds = map(int, sys.stdin.readline().split())
    ume = [tuple(map(int, sys.stdin.readline().split())) for _ in range(U)]
    momo = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
    sakura = [tuple(map(int, sys.stdin.readline().split())) for _ in range(S)]
    winds = [tuple(map(int, sys.stdin.readline().split())) for _ in range(R)]
    # Each day, wind is given by (w_i, a_i)
    # For each house, check if it is inside ume fan and outside all other flowers fans
    # Sector angles are given by du, dm, ds for ume, momo, sakura respectively.

    # For each day
    #   For each house
    #     Check if house in ume scent sector (center at w, radius a, half angle du/2)
    #     For other flowers, check same with their angles and positions
    #     If in ume only => count++ for that house

    cnt = [0]*H
    for w_i, a_i in winds:
        for i, (hx, hy) in enumerate(houses):
            # Check ume scent
            if not in_sector(hx, hy, a_i, w_i, du / 2):
                continue
            conflict = False
            # Check ume other
            for ux, uy in ume:
                if in_sector(hx - ux, hy - uy, a_i, w_i, du / 2):
                    conflict = True
                    break
            if conflict:
                continue
            # Check momo
            for mx, my in momo:
                if in_sector(hx - mx, hy - my, a_i, w_i, dm / 2):
                    conflict = True
                    break
            if conflict:
                continue
            # Check sakura
            for sx, sy in sakura:
                if in_sector(hx - sx, hy - sy, a_i, w_i, ds / 2):
                    conflict = True
                    break
            if conflict:
                continue
            cnt[i] += 1
    mx = max(cnt)
    if mx == 0:
        print("NA")
    else:
        ans = [str(i+1) for i, v in enumerate(cnt) if v == mx]
        print(" ".join(ans))