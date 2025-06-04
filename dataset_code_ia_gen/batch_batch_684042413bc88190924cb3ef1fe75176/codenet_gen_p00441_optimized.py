import sys
import math

input = sys.stdin.readline

def max_square_area(points):
    pts = list(points)
    point_set = set(points)
    n = len(pts)
    max_area = 0
    # Pour chaque paire de points, déterminer les points qui complètent un carré
    for i in range(n):
        x1, y1 = pts[i]
        for j in range(i+1, n):
            x2, y2 = pts[j]
            dx = x2 - x1
            dy = y2 - y1
            # Les deux autres points possibles pour former un carré
            p3 = (x1 - dy, y1 + dx)
            p4 = (x2 - dy, y2 + dx)
            if p3 in point_set and p4 in point_set:
                area = dx*dx + dy*dy
                if area > max_area:
                    max_area = area
            p3 = (x1 + dy, y1 - dx)
            p4 = (x2 + dy, y2 - dx)
            if p3 in point_set and p4 in point_set:
                area = dx*dx + dy*dy
                if area > max_area:
                    max_area = area
    return max_area

while True:
    n = int(input())
    if n == 0:
        break
    points = set()
    for _ in range(n):
        x,y = map(int,input().split())
        points.add((x,y))
    res = max_square_area(points)
    print(res)