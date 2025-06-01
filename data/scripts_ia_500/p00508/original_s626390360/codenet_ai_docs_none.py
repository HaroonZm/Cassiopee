import sys
from sys import stdin
input = stdin.readline

def closest_part(points, n):
    if n <= 1:
        return float('inf')
    m = n // 2
    x = points[m][0]
    d = min(closest_part(points[:m], m), closest_part(points[m:], n-m))

    points.sort(key=lambda p:p[1])
    b = []
    for p in points:
        if (p[0] - x)**2 >= d:
            continue
        for q in b:
            dx = p[0] - q[0]
            dy = p[1] - q[1]
            if dy**2 >= d:
                break
            d = min(d, (dx**2 + dy**2))
        b.insert(0, p)
    return d

def main(args):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    points.sort()

    result = closest_part(points, n)
    print(result)

if __name__ == '__main__':
    main(sys.argv[1:])