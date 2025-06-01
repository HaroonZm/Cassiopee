import sys

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1] + upper[:-1]
    return hull

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n = int(input_lines[idx].strip())
        idx += 1
        if n == 0:
            break
        points = []
        for _ in range(n):
            line = input_lines[idx].strip().replace(' ','')
            idx += 1
            x_str, y_str = line.split(',')
            x = float(x_str)
            y = float(y_str)
            points.append((x,y))
        hull = convex_hull(points)
        hull_set = set(hull)
        print(n - len(hull_set))

if __name__ == "__main__":
    main()