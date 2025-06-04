import math
import sys

def angle_to_right(v1, v2):
    # Calculate angle to the right from vector v1 to v2 in [0, 2pi)
    cross = v1[0]*v2[1] - v1[1]*v2[0]
    dot = v1[0]*v2[0] + v1[1]*v2[1]
    ang = math.atan2(cross, dot)
    if ang < 0:
        return 2*math.pi + ang
    return ang

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def main():
    lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(lines):
            break
        line = lines[idx].strip()
        if not line:
            idx += 1
            continue
        n = int(line)
        if n == 0:
            break
        idx += 1
        flags = [(0,0)]
        for _ in range(n):
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
            xys = lines[idx].strip().split()
            x = int(xys[0])
            y = int(xys[1])
            flags.append((x,y))
            idx += 1

        visited = [False]*(n+1)
        visited[0] = True
        cur_pos = (0,0)
        cur_dir = (0,1)  # facing north
        total_dist = 0.0
        for _ in range(n):
            candidates = []
            for i in range(n+1):
                if visited[i]:
                    continue
                v = (flags[i][0]-cur_pos[0], flags[i][1]-cur_pos[1])
                if v == (0,0):
                    continue
                ang = angle_to_right(cur_dir, v)
                d = dist(cur_pos, flags[i])
                candidates.append((ang, d, i))
            # Among candidates, pick minimal angle; if tie minimal distance
            candidates.sort(key=lambda x: (x[0], x[1]))
            next_i = candidates[0][2]
            total_dist += dist(cur_pos, flags[next_i])
            cur_dir = (flags[next_i][0]-cur_pos[0], flags[next_i][1]-cur_pos[1])
            # normalize cur_dir
            length = math.hypot(cur_dir[0], cur_dir[1])
            cur_dir = (cur_dir[0]/length, cur_dir[1]/length)
            cur_pos = flags[next_i]
            visited[next_i] = True

        print(f"{total_dist:.1f}")

if __name__ == "__main__":
    main()