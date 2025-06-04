import math
import sys

def normalize(v):
    length = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return (v[0]/length, v[1]/length, v[2]/length)

def angle_between(v1, v2):
    # v1 and v2 are unit vectors
    dot = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    # Clamp dot product to avoid floating point errors out of domain
    dot = max(min(dot, 1.0), -1.0)
    return math.acos(dot)

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n = input_lines[idx].strip()
        idx += 1
        if n == '0':
            break
        n = int(n)
        stars = []
        for _ in range(n):
            sx, sy, sz = map(float, input_lines[idx].strip().split())
            idx += 1
            stars.append(normalize((sx, sy, sz)))
        m = int(input_lines[idx].strip())
        idx += 1
        telescopes = []
        for _ in range(m):
            tx, ty, tz, phi = input_lines[idx].strip().split()
            idx += 1
            t_dir = normalize((float(tx), float(ty), float(tz)))
            phi = float(phi)
            telescopes.append((t_dir, phi))

        visible = set()
        for i, s_dir in enumerate(stars):
            for t_dir, phi in telescopes:
                if angle_between(s_dir, t_dir) < phi:
                    visible.add(i)
                    break
        print(len(visible))

if __name__ == '__main__':
    main()