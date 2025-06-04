import sys
import math

def in_sector(px, py, angle_c, radius, half_angle):
    dist = math.hypot(px, py)
    if dist > radius + 1e-10:
        return False
    angle_p = math.degrees(math.atan2(py, px))
    diff = (angle_p - angle_c + 360) % 360
    return diff <= half_angle or diff >= 360 - half_angle

def main():
    input = sys.stdin.readline
    res = []
    while True:
        line = ''
        while line.strip() == '':
            line = input()
            if line == '':
                break
        if line == '':
            break
        H_R = line.strip().split()
        if len(H_R) < 2:
            break
        H, R = map(int, H_R)
        if H == 0 and R == 0:
            break
        houses = [tuple(map(int, input().split())) for _ in range(H)]
        U, M, S, du, dm, ds = map(int, input().split())
        plum = [tuple(map(int, input().split())) for _ in range(U)]
        peach = [tuple(map(int, input().split())) for _ in range(M)]
        cherry = [tuple(map(int, input().split())) for _ in range(S)]
        winds = [tuple(map(int, input().split())) for _ in range(R)]

        plum_ang = du / 2
        peach_ang = dm / 2
        cherry_ang = ds / 2

        # Precompute the sets of houses for each day where our plum scent only reaches
        count_only = [0]*H

        for w,a in winds:
            a = float(a)
            w = float(w)
            # For each house, check whether our plum scent reaches, and others do not
            for i,(hx, hy) in enumerate(houses):
                # Our plum position is origin
                x, y = hx, hy
                # Check if in our plum sector
                if not in_sector(x, y, w, a, plum_ang):
                    continue
                # Check if in any other flower scent sector
                conflict = False
                # Other plum trees
                for ux, uy in plum:
                    px = hx - ux
                    py = hy - uy
                    if in_sector(px, py, w, a, plum_ang):
                        conflict = True
                        break
                if conflict:
                    continue
                # Peach trees
                for mx, my in peach:
                    px = hx - mx
                    py = hy - my
                    if in_sector(px, py, w, a, peach_ang):
                        conflict = True
                        break
                if conflict:
                    continue
                # Cherry trees
                for sx, sy in cherry:
                    px = hx - sx
                    py = hy - sy
                    if in_sector(px, py, w, a, cherry_ang):
                        conflict = True
                        break
                if conflict:
                    continue
                count_only[i] += 1

        max_count = max(count_only) if count_only else 0
        if max_count == 0:
            print('NA')
        else:
            ans = [str(i+1) for i,v in enumerate(count_only) if v == max_count]
            print(' '.join(ans))

if __name__ == '__main__':
    main()